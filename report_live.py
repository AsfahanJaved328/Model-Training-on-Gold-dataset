"""report_live.py - writes LIVE_STATUS.md from the forecast log and its out-of-sample evaluation."""
import os
import numpy as np, pandas as pd
from scipy import stats
FENCE = chr(96) * 3
LOG, EVAL, OUT = "results/forecast_log_v2.csv", "results/forecast_eval.csv", "LIVE_STATUS.md"
lines = ["# Live status (paper tracking, not advice)", ""]
if os.path.exists(LOG):
    L = pd.read_csv(LOG)
    last = L.sort_values("data_date").groupby("asset").tail(1)
    lines += ["## Latest forecasts", "", FENCE, last.to_string(index=False), FENCE, ""]
    for _, r in last.iterrows():
        e = min(1.0, 0.10 / (r["har5d_ann_vol_pct"] / 100))
        lines.append("- " + str(r["asset"]) + ": exposure that would target 10% annual vol (cap 1x) = " + format(e, ".2f") + " (illustrative only)")
if os.path.exists(EVAL):
    E = pd.read_csv(EVAL)
    lines += ["", "## Out-of-sample evaluation (matured forecasts)", ""]
    for a, g in E.groupby("asset"):
        n = len(g); sub = g.iloc[::5]
        row = "- " + a + ": N=" + str(n) + " (non-overlapping " + str(len(sub)) + "), HAR mean|logerr|=" + format(g.har_abs_logerr.mean(), ".3f") + ", Persistence=" + format(g.persist_abs_logerr.mean(), ".3f")
        if len(sub) > 5:
            diff = (sub.persist_abs_logerr - sub.har_abs_logerr).values
            p2 = stats.ttest_1samp(diff, 0).pvalue; p1 = p2 / 2 if diff.mean() > 0 else 1 - p2 / 2
            row += ", one-sided p(HAR better, non-overlap)=" + format(p1, ".3f")
        v95 = int(g.viol95.sum()); pb = stats.binomtest(v95, n, 0.05).pvalue
        row += "; VaR95 violations " + str(v95) + "/" + str(n) + " (" + format(v95 / n * 100, ".1f") + "% vs 5%), binomial p=" + format(pb, ".3f")
        lines.append(row)
    lines += ["", "Verdict is only meaningful once N >= 120 matured forecasts per asset (see PREREG.md)."]
else:
    lines += ["", "No matured forecasts yet (a forecast needs 5 trading days to mature)."]
open(OUT, "w").write("\n".join(lines))
print("\n".join(lines))
