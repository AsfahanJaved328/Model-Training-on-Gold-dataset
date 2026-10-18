# Pre-registration of the live evaluation (committed BEFORE results exist)

Models under test (frozen, version v2): 5-day volatility = HAR, EWMA (alpha 0.06), Persistence (baseline); 1-day VaR 95% and 99% = filtered historical simulation (EWMA sigma, 500-day standardized-residual quantile).

Evaluation starts when each asset has at least 120 matured forecasts (about 6 months of daily runs). Before that, results are only monitored, never claimed.

Pass criteria:
1. Volatility: HAR mean absolute log-error < Persistence mean absolute log-error, AND one-sided paired t-test p < 0.05 on the non-overlapping subsample (every 5th forecast).
2. VaR 95%: observed violation rate has a two-sided exact binomial test p > 0.05 against 5%. VaR 99% is reported only (too few expected violations before about 300 forecasts).
3. No change of model, parameters or data source during evaluation. Any change is a new version (v3) and restarts the clock.

Paper tracking only. Not financial advice.
