# Model Training on Gold (and BTC) dataset
Day 1: data download (to 2026-10-15), Naive / XGBoost / Chronos-Bolt zero-shot baselines.
Results: `results/metrics.csv`, plots in `results/`.

## Day 2
250-day rolling-origin backtest: Naive, Chronos-Bolt, Chronos-2, Chronos-2+covariates, XGBoost (walk-forward). Results in `results/metrics_day2.csv` (MAE_vs_Naive, p-values vs Naive).

## Day 2
250-day rolling-origin backtest: Naive, Chronos-Bolt, Chronos-2, Chronos-2+covariates, XGBoost (walk-forward). Results in `results/metrics_day2.csv` (MAE_vs_Naive, p-values vs Naive).

## Day 2 finding
Naive beat all price models (Chronos-Bolt, Chronos-2, Chronos-2+cov, XGBoost) on both GOLD and BTC; no tradable edge.

## Day 3
5-day-ahead realized volatility forecasting. Results in `results/metrics_day3_vol.csv`.
