# Gold & BTC: forecasting and risk toolkit
Research project (Kaggle + GitHub). Goal: test whether time-series models (Chronos, XGBoost, HAR, EWMA) give a tradable or risk-management edge on Gold and BTC.

**Result so far:** no edge in price direction or in return-seeking sizing; volatility and VaR forecasts are the useful part. See SUMMARY.md and REPORT.md.

## Files
- SUMMARY.md, REPORT.md: conclusions and full tables. PROJECT_LOG.md: day-by-day log.
- results/: metrics CSVs and plots.
- forecast_today.py: daily vol / VaR / trend / inverse-vol-weight forecast -> results/forecast_log_v2.csv.
- evaluate_log.py: scores past forecasts against realized outcomes -> results/forecast_eval.csv.
- .github/workflows/daily_forecast.yml: runs both daily (GitHub Actions).

Paper-tracking only. Not financial advice.

## Update (Days 13-32)
See FINAL_REPORT.md (all results), PREREG.md (live evaluation rules), LIVE_STATUS.md (auto-updated once the daily workflow runs), tests/ and core.py.
