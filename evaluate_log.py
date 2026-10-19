"""evaluate_log.py v3 - scores matured forecasts against realized volatility and next-day returns."""
import os, datetime as dt
import numpy as np, pandas as pd, yfinance as yf

LOG, OUT = "results/forecast_log_v3.csv", "results/forecast_eval_v3.csv"
TICK = {"GOLD": ("GC=F", True), "BTC": ("BTC-USD", False)}
MODELS = ["persist", "ewma", "garch", "har", "ens"]
H = 5
if not os.path.exists(LOG):
    raise SystemExit("forecast_log_v3.csv abhi nahi hai.")
L = pd.read_csv(LOG, parse_dates=["data_date"])
today = pd.Timestamp(dt.datetime.now(dt.timezone.utc).date())
rows = []
for a, (t, wd) in TICK.items():
    sub = L[L["asset"] == a]
    if sub.empty:
        continue
    start = (sub["data_date"].min() - pd.Timedelta(days=10)).strftime("%Y-%m-%d")
    px = yf.download(t, start=start, progress=False, auto_adjust=True)
    if isinstance(px.columns, pd.MultiIndex):
        px.columns = px.columns.get_level_values(0)
    c = px["Close"].dropna()
    c = c[c.index < today]
    if wd:
        c = c[c.index.dayofweek < 5]
    lr, pr = np.log(c).diff().dropna(), c.pct_change().dropna()
    for _, row in sub.iterrows():
        fut = lr[lr.index > row["data_date"]]
        nxt = pr[pr.index > row["data_date"]]
        if len(fut) < H:
            continue
        real = float(np.sqrt(np.mean(fut.iloc[:H].values ** 2))) * 100
        if real <= 0:
            continue
        out = {"data_date": row["data_date"].date(), "asset": a, "realized_5d_vol_pct": round(real, 4)}
        for m in MODELS:
            p = row["vol_%s_pct" % m]
            if p == p and p > 0:
                x = (real / p) ** 2
                out["qlike_" + m] = x - np.log(x) - 1
                out["abslogerr_" + m] = abs(np.log(p / real))
            else:
                out["qlike_" + m] = np.nan
                out["abslogerr_" + m] = np.nan
        n1 = float(nxt.iloc[0]) * 100
        out["viol95"] = int(n1 < row["var95_1d_pct"])
        out["viol99"] = int(n1 < row["var99_1d_pct"])
        rows.append(out)
if rows:
    E = pd.DataFrame(rows)
    E.to_csv(OUT, index=False)
    cols = ["qlike_" + m for m in MODELS] + ["viol95", "viol99"]
    print(E.groupby("asset")[cols].mean().round(3))
    print("N evaluated:", E.groupby("asset").size().to_dict())
else:
    print("Abhi evaluate karne ke liye kaafi purani forecasts nahi (5 trading days chahiye).")
