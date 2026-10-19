"""report_live.py v3 - writes LIVE_STATUS.md."""
import os
import numpy as np, pandas as pd
from scipy import stats
FENCE = chr(96) * 3
LOG, EVAL, OUT = "results/forecast_log_v3.csv", "results/forecast_eval_v3.csv", "LIVE_STATUS.md"
MODELS = ["persist", "ewma", "garch", "har", "ens"]
lines = ["# Live status v3 (paper tracking, not advice)", ""]
if os.path.exists(LOG):
    L = pd.read_csv(LOG)
    last = L.sort_values("data_date").groupby("asset").tail(1)
    lines += ["## Latest forecasts (daily vol %)", "", FENCE, last.to_string(index=False), FENCE, ""]
if os.path.exists(EVAL):
    E = pd.read_csv(EVAL)
    lines += ["## Out-of-sample evaluation (matured forecasts)", ""]
    for a, g in E.groupby("asset"):
        g = g.sort_values("data_date")
        n = len(g)
        lines.append("### " + a + " (N=" + str(n) + ")")
        q = {m: g["qlike_" + m].mean() for m in MODELS}
        lines.append("- mean QLIKE (lower is better): " + ", ".join(m + " " + format(v, ".3f") for m, v in q.items()))
        sub = g.iloc[::5]
        for base in ["ewma", "persist"]:
            d = (sub["qlike_" + base] - sub["qlike_ens"]).dropna().values
            if len(d) > 5:
                p2 = stats.ttest_1samp(d, 0).pvalue
                p1 = p2 / 2 if d.mean() > 0 else 1 - p2 / 2
                lines.append("- Ensemble better than " + base + ": one-sided p=" + format(p1, ".3f") + " (non-overlapping n=" + str(len(d)) + ")")
        v95 = int(g.viol95.sum())
        pb = stats.binomtest(v95, n, 0.05).pvalue
        lines.append("- VaR95 violations " + str(v95) + "/" + str(n) + " (" + format(v95 / n * 100, ".1f") + "% vs 5%), binomial p=" + format(pb, ".3f"))
        lines.append("- status: " + ("evaluation ACTIVE (rules in PREREG.md)" if n >= 120 else "monitoring only (need 120 matured forecasts, have " + str(n) + ")"))
else:
    lines += ["No matured forecasts yet (a forecast needs 5 trading days to mature)."]
open(OUT, "w").write("\n".join(lines))
print("\n".join(lines))
