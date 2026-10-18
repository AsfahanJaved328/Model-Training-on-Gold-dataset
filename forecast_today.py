"""forecast_today.py - daily risk forecasts (vol, VaR, trend, inverse-vol weights). Paper tracking only, NOT trading advice."""
import os, datetime as dt
import numpy as np, pandas as pd, yfinance as yf

ASSETS = {"GOLD": ("GC=F", 252), "BTC": ("BTC-USD", 365)}
H = 5
LOG = "results/forecast_log_v2.csv"

def load(ticker):
    today = pd.Timestamp(dt.datetime.now(dt.timezone.utc).date())
    start = (today - pd.Timedelta(days=4 * 365 + 60)).strftime("%Y-%m-%d")
    df = yf.download(ticker, start=start, progress=False, auto_adjust=True)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    c = df["Close"].dropna()
    return c[c.index < today]

def make(close, ppy):
    lr = np.log(close).diff(); pr = close.pct_change()
    D = pd.DataFrame({"v5": np.log(lr.rolling(5).std()), "v22": np.log(lr.rolling(22).std()),
                      "v66": np.log(lr.rolling(66).std()),
                      "ew": 0.5 * np.log((lr ** 2).ewm(alpha=0.06).mean())}).replace([np.inf, -np.inf], np.nan)
    D["y"] = D["v5"].shift(-H)
    D = D.iloc[66:]
    D = D[D[["v5", "v22", "v66", "ew"]].notna().all(axis=1)]
    last = D.iloc[-1]
    tr = D.iloc[:-H].dropna(subset=["y"])
    X = np.column_stack([np.ones(len(tr)), tr["v5"], tr["v22"], tr["v66"]])
    beta = np.linalg.lstsq(X, tr["y"].values, rcond=None)[0]
    har = float(np.array([1, last["v5"], last["v22"], last["v66"]]) @ beta)
    sig = np.sqrt((pr ** 2).ewm(alpha=0.06).mean())
    z = (pr / sig.shift(1)).replace([np.inf, -np.inf], np.nan).dropna().iloc[-500:]
    sig_next = float(sig.iloc[-1])
    sma = close.rolling(200).mean()
    return {"data_date": D.index[-1].date(),
            "ewma_daily_vol_pct": round(float(np.exp(last["ew"])) * 100, 3),
            "har5d_daily_vol_pct": round(float(np.exp(har)) * 100, 3),
            "har5d_ann_vol_pct": round(float(np.exp(har)) * np.sqrt(ppy) * 100, 2),
            "persist5d_daily_vol_pct": round(float(np.exp(last["v5"])) * 100, 3),
            "var95_1d_pct": round(sig_next * float(z.quantile(0.05)) * 100, 3),
            "var99_1d_pct": round(sig_next * float(z.quantile(0.01)) * 100, 3),
            "above_sma200": int(close.iloc[-1] > sma.iloc[-1]), "sig_next": sig_next}

rows, sigs = [], {}
for name, (tk, ppy) in ASSETS.items():
    res = make(load(tk), ppy)
    sigs[name] = res.pop("sig_next")
    rows.append({"run_date": dt.date.today().isoformat(), "asset": name, **res})
tot = sum(1 / v for v in sigs.values())
for r_ in rows:
    r_["invvol_weight"] = round((1 / sigs[r_["asset"]]) / tot, 3)
new = pd.DataFrame(rows)
print(new.to_string(index=False))
os.makedirs("results", exist_ok=True)
if os.path.exists(LOG):
    old = pd.read_csv(LOG)
    key = set(zip(old["data_date"].astype(str), old["asset"]))
    keep = [(str(d), a) not in key for d, a in zip(new["data_date"].astype(str), new["asset"])]
    new = new[keep]
    if len(new): new.to_csv(LOG, mode="a", header=False, index=False)
else:
    new.to_csv(LOG, index=False)
