"""forecast_today.py - 5-day-ahead volatility forecast. Paper tracking only, NOT trading advice."""
import os, datetime as dt
import numpy as np, pandas as pd, yfinance as yf

ASSETS = {"GOLD": ("GC=F", 252), "BTC": ("BTC-USD", 365)}
H = 5

def load(ticker):
    today = pd.Timestamp(dt.datetime.now(dt.timezone.utc).date())
    start = (today - pd.Timedelta(days=3 * 365 + 30)).strftime("%Y-%m-%d")
    df = yf.download(ticker, start=start, progress=False, auto_adjust=True)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    c = df["Close"].dropna()
    return c[c.index < today]          # aaj ki adhoori candle hata do

def forecast(close):
    r = np.log(close).diff()
    D = pd.DataFrame({
        "v5": np.log(r.rolling(5).std()), "v22": np.log(r.rolling(22).std()),
        "v66": np.log(r.rolling(66).std()),
        "ew": 0.5 * np.log((r ** 2).ewm(alpha=0.06).mean()),
    }).replace([np.inf, -np.inf], np.nan)
    D["y"] = D["v5"].shift(-H)
    D = D.iloc[66:]
    D = D[D[["v5", "v22", "v66", "ew"]].notna().all(axis=1)]
    last = D.iloc[-1]
    tr = D.iloc[:-H].dropna(subset=["y"])
    X = np.column_stack([np.ones(len(tr)), tr["v5"], tr["v22"], tr["v66"]])
    beta = np.linalg.lstsq(X, tr["y"].values, rcond=None)[0]
    har = float(np.array([1, last["v5"], last["v22"], last["v66"]]) @ beta)
    return {"data_date": D.index[-1].date(), "EWMA": float(last["ew"]), "HAR": har}, r

rows = []
for name, (ticker, ppy) in ASSETS.items():
    close = load(ticker)
    f, r = forecast(close)
    tgt = r.rolling(22).std().median()
    for m in ["EWMA", "HAR"]:
        dv = float(np.exp(f[m]))
        rows.append({"run_date": dt.date.today().isoformat(), "data_date": f["data_date"], "asset": name,
                     "model": m, "pred_daily_vol_pct": round(dv * 100, 3),
                     "pred_ann_vol_pct": round(dv * np.sqrt(ppy) * 100, 2),
                     "exposure_if_vol_target": round(float(np.clip(tgt / dv, 0, 1)), 2)})
out = pd.DataFrame(rows)
print(out.to_string(index=False))
os.makedirs("results", exist_ok=True)
path = "results/forecast_log.csv"
out.to_csv(path, mode="a", header=not os.path.exists(path), index=False)
