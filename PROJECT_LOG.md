# Project log (previous README content)
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

## Day 3 finding
EWMA/HAR/Chronos-2 beat Persistence for 5-day vol (MAE -19% to -26%); HAR best overall, Chronos-2 not better than HAR.

## Day 4
Vol-targeting position sizing (cap 1x, costs included) vs Buy&Hold. Results in `results/metrics_day4_sizing.csv`.

## Day 4 finding
GOLD: EWMA vol-targeting cut vol/DD/vol-of-vol vs Buy&Hold; BTC: almost no effect (target vol was too high, weights clipped at 1). Sharpe differences are within noise (300 days).

## Day 5
Robustness: 400-day window, two a-priori target definitions, matched constant-exposure controls, block-bootstrap CI for Sharpe difference. See `results/metrics_day5_robustness.csv`.

## Day 5 finding
GOLD+EWMA vol-targeting showed borderline-significant Sharpe gain vs Buy&Hold and vs constant-exposure control; GOLD+HAR and BTC did not. Correction: the Day 4 note blaming spike-inflated target vol for BTC is wrong (median target gave the same result).

## Day 6
Added `SUMMARY.md` and `forecast_today.py` (paper-tracking 5-day vol forecast, appends to `results/forecast_log.csv`).

## Day 5 finding
GOLD+EWMA vol-targeting showed borderline-significant Sharpe gain vs Buy&Hold and vs constant-exposure control; GOLD+HAR and BTC did not. Correction: the Day 4 note blaming spike-inflated target vol for BTC is wrong (median target gave the same result).

## Day 6
Added `SUMMARY.md` and `forecast_today.py` (paper-tracking 5-day vol forecast, appends to `results/forecast_log.csv`).

## Day 5-7
Robustness checks, clip-check (BTC cap explanation), fixed `forecast_today.py` (drops incomplete candle), and Day 7 long-history expanding walk-forward backtest with a pre-registered pass rule. See `SUMMARY.md`.


## Day 13-32
Research modules 13-28 (audit, leakage, placebo, vol horse race, Chronos-2 vol, equal-vol strategy tests, trend grid, costs, subperiods, ES, VaR grid, dependence, drawdown stop), Holm/BH correction (29), live-evaluation infrastructure + PREREG.md (30), FINAL_REPORT.md (31). See FINAL_REPORT.md.
