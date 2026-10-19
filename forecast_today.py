"""forecast_today.py v3 - daily vol / VaR forecasts from several models. Paper tracking only, NOT trading advice."""
import os, datetime as dt, warnings
import numpy as np, pandas as pd, yfinance as yf
warnings.filterwarnings("ignore")

ASSETS = {"GOLD": ("GC=F", 252, True), "BTC": ("BTC-USD", 365, False)}   # (ticker, periods/yr, weekdays_only)
H = 5
LOG = "results/forecast_log_v3.csv"

def load(ticker, weekdays_only):
    today = pd.Timestamp(dt.datetime.now(dt.timezone.utc).date())
    start = (today - pd.Timedelta(days=6 * 365)).strftime("%Y-%m-%d")
    df = yf.download(ticker, start=start, progress=False, auto_adjust=True)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    c = df["Close"].dropna()
    c = c[c.index < today]
    if weekdays_only:
        c = c[c.index.dayofweek < 5]
    return c

def garch_var(lr):
    try:
        from arch import arch_model
        x = lr.iloc[-2500:].values * 100
        res = arch_model(x, mean="Zero", vol="GARCH", p=1, q=1, dist="t").fit(disp="off", show_warning=False)
        f = res.forecast(horizon=H, reindex=False).variance.values[-1]
        return float(np.mean(f)) / 1e4
    except Exception:
        return float("nan")

def make(close, ppy):
    lr = np.log(close).diff().dropna()
    pr = close.pct_change().dropna()
    sq = lr ** 2
    r = np.log(close).diff()
    D = pd.DataFrame({"v5": np.log(r.rolling(5).std()), "v22": np.log(r.rolling(22).std()),
                      "v66": np.log(r.rolling(66).std())}).replace([np.inf, -np.inf], np.nan)
    D["y"] = D["v5"].shift(-H)
    D = D.iloc[66:].dropna(subset=["v5", "v22", "v66"])
    last = D.iloc[-1]
    tr = D.iloc[:-H].dropna(subset=["y"])
    X = np.column_stack([np.ones(len(tr)), tr["v5"], tr["v22"], tr["v66"]])
    beta = np.linalg.lstsq(X, tr["y"].values, rcond=None)[0]
    smear = float(np.mean(np.exp(2 * (tr["y"].values - X @ beta))))          # Duan smearing (bias fix)
    har_var = float(np.exp(2 * (np.array([1, last["v5"], last["v22"], last["v66"]]) @ beta)) * smear)
    v_pers = float(sq.iloc[-5:].mean())
    v_ewma = float(sq.ewm(alpha=0.06).mean().iloc[-1])
    v_garch = garch_var(lr)
    if v_garch != v_garch:
        raise SystemExit("GARCH fail hua (arch install hai? workflow mein 'pip install ... arch' hona chahiye). Koi row log nahi hui.")
    v_ens = float(np.mean([v_ewma, v_garch, har_var]))
    sig = np.sqrt((pr ** 2).ewm(alpha=0.06).mean())
    z = (pr / sig.shift(1)).replace([np.inf, -np.inf], np.nan).dropna().iloc[-500:]
    sig_next = float(sig.iloc[-1])
    sma = close.rolling(200).mean()
    pct = lambda v: round(float(np.sqrt(v)) * 100, 4)
    return {"data_date": close.index[-1].date(),
            "vol_persist_pct": pct(v_pers), "vol_ewma_pct": pct(v_ewma), "vol_garch_pct": pct(v_garch),
            "vol_har_pct": pct(har_var), "vol_ens_pct": pct(v_ens),
            "ens_ann_vol_pct": round(float(np.sqrt(v_ens)) * np.sqrt(ppy) * 100, 2),
            "var95_1d_pct": round(sig_next * float(z.quantile(0.05)) * 100, 3),
            "var99_1d_pct": round(sig_next * float(z.quantile(0.01)) * 100, 3),
            "above_sma200": int(close.iloc[-1] > sma.iloc[-1]), "sig_next": sig_next}

rows, sigs = [], {}
for name, (tk, ppy, wd) in ASSETS.items():
    res = make(load(tk, wd), ppy)
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
    if len(new):
        new.to_csv(LOG, mode="a", header=False, index=False)
else:
    new.to_csv(LOG, index=False)
