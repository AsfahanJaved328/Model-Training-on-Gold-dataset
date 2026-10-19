# Pre-registration v3 (written before any live forecast has matured)

Supersedes v2. Reason for the change: the Day 16 backtest showed GARCH-t / Ensemble beating EWMA on QLIKE for both assets.
This choice was made AFTER seeing backtest results, so the backtest win is not evidence on its own; the live test below is the real out-of-sample check.

Models (frozen as version v3), 5-day-ahead average daily variance:
- Persistence (mean of last 5 squared log returns), EWMA (alpha 0.06), GARCH(1,1)-t refit daily on the last 2500 days,
  HAR on log-vol with Duan smearing bias correction, Ensemble = mean of EWMA, GARCH-t and HAR.
- Note: backtested HAR-cal used an expanding-mean ratio calibration; the live version uses smearing (same purpose, different estimator).
- 1-day VaR 95% and 99%: filtered historical simulation (EWMA sigma, 500-day standardized-residual quantile).
- GOLD uses weekday rows only (weekend rows removed). BTC uses all days.

Evaluation starts when an asset has at least 120 matured forecasts (about 6 months). Before that, results are monitored, never claimed.

Primary hypothesis (per asset): Ensemble has lower mean QLIKE than EWMA, one-sided paired t-test p < 0.025 (Bonferroni for 2 assets)
on the non-overlapping subsample (every 5th forecast).
Secondary (descriptive): every model vs Persistence; VaR95 violation rate with a two-sided exact binomial p > 0.05 against 5%.
VaR99 is reported only (too few expected violations before about 300 forecasts).

No change of models, parameters or data source during evaluation. Any change is a new version (v4) and restarts the clock.
Paper tracking only. Not financial advice.
