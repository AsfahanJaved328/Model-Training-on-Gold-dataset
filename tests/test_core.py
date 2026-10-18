import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np, pandas as pd
from core import vol_frame, walk_har, kupiec

def _prices(n=2500, seed=0):
    r = np.random.default_rng(seed).standard_t(5, n) * 0.01
    return pd.Series(100 * np.cumprod(1 + r), index=pd.bdate_range("2010-01-01", periods=n))

def test_kupiec_is_calibrated_under_the_null():
    rng = np.random.default_rng(1)
    ps = [kupiec((rng.random(1000) < 0.05).astype(int), 0.05) for _ in range(200)]
    assert np.mean(np.array(ps) < 0.05) < 0.12

def test_vol_features_have_no_lookahead():
    c = _prices(); k = len(c) - 300
    Df, Dt = vol_frame(c), vol_frame(c.iloc[:k]); cols = ["v5", "v22", "v66", "ew"]
    assert np.allclose(Df.loc[Dt.index, cols].values, Dt[cols].values)

def test_walk_forward_har_is_truncation_invariant():
    c = _prices(); k = len(c) - 300
    Df, Dt = vol_frame(c), vol_frame(c.iloc[:k])
    hf = pd.Series(walk_har(Df, 500), index=Df.index).loc[Dt.index].values
    assert np.allclose(hf, walk_har(Dt, 500), equal_nan=True)
