"""evaluate_log.py - compares logged forecasts with what actually happened (out-of-sample)."""
import os, datetime as dt
import numpy as np, pandas as pd, yfinance as yf

LOG, OUT = "results/forecast_log_v2.csv", "results/forecast_eval.csv"
TICK = {"GOLD": "GC=F", "BTC": "BTC-USD"}
if not os.path.exists(LOG):
    raise SystemExit("forecast_log_v2.csv abhi nahi hai.")
L = pd.read_csv(LOG, parse_dates=["data_date"])
today = pd.Timestamp(dt.datetime.now(dt.timezone.utc).date())
rows = []
for a, t in TICK.items():
    sub = L[L["asset"] == a]
    if sub.empty: continue
    start = (sub["data_date"].min() - pd.Timedelta(days=5)).strftime("%Y-%m-%d")
    px = yf.download(t, start=start, progress=False, auto_adjust=True)
    if isinstance(px.columns, pd.MultiIndex): px.columns = px.columns.get_level_values(0)
    c = px["Close"].dropna(); c = c[c.index < today]
    lr, pr = np.log(c).diff(), c.pct_change()
    for _, row in sub.iterrows():
        fut, nxt = lr[lr.index > row["data_date"]], pr[pr.index > row["data_date"]]
        if len(fut) < 5: continue
        real = float(fut.iloc[:5].std()) * 100
        n1 = float(nxt.iloc[0]) * 100
        rows.append({"data_date": row["data_date"].date(), "asset": a, "realized_5d_vol_pct": round(real, 3),
                     "har_abs_logerr": abs(np.log(row["har5d_daily_vol_pct"] / real)),
                     "persist_abs_logerr": abs(np.log(row["persist5d_daily_vol_pct"] / real)),
                     "viol95": int(n1 < row["var95_1d_pct"]), "viol99": int(n1 < row["var99_1d_pct"])})
if rows:
    E = pd.DataFrame(rows); E.to_csv(OUT, index=False)
    print(E.groupby("asset")[["har_abs_logerr", "persist_abs_logerr", "viol95", "viol99"]].mean().round(3))
    print("N evaluated:", E.groupby("asset").size().to_dict())
else:
    print("Abhi evaluate karne ke liye kaafi purani forecasts nahi (5 trading days chahiye).")
