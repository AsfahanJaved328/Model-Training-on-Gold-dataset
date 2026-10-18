"""core.py - shared functions (no network access)."""
import numpy as np, pandas as pd
from scipy.special import xlogy
from scipy.stats import chi2
H = 5

def ewma_vol(c):
    r = np.log(c).diff(); return np.sqrt((r ** 2).ewm(alpha=0.06).mean())

def vol_frame(close):
    r = np.log(close).diff()
    D = pd.DataFrame({"v5": np.log(r.rolling(5).std()), "v22": np.log(r.rolling(22).std()),
                      "v66": np.log(r.rolling(66).std()),
                      "ew": 0.5 * np.log((r ** 2).ewm(alpha=0.06).mean())}).replace([np.inf, -np.inf], np.nan)
    D["y"] = D["v5"].shift(-H); D = D.iloc[66:]
    return D[D[["v5", "v22", "v66", "ew"]].notna().all(axis=1)]

def walk_har(D, start, step=21):
    n = len(D); X = np.column_stack([np.ones(n), D["v5"], D["v22"], D["v66"]]); y = D["y"].values
    out = np.full(n, np.nan)
    for s in range(start, n, step):
        tr = np.arange(0, s - H); tr = tr[~np.isnan(y[tr])]
        beta = np.linalg.lstsq(X[tr], y[tr], rcond=None)[0]
        e = min(s + step, n); out[s:e] = X[s:e] @ beta
    return out

def kupiec(I, p):
    N = len(I); x = int(I.sum())
    ll0 = xlogy(N - x, 1 - p) + xlogy(x, p); ll1 = xlogy(N - x, 1 - x / N) + xlogy(x, x / N)
    return 1 - chi2.cdf(max(-2 * (ll0 - ll1), 0), 1)
