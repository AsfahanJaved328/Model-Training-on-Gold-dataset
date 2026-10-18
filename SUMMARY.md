# Summary (Days 1-6)

**Price forecasting (1-day):** Naive beat Chronos-Bolt, Chronos-2, Chronos-2+cov and XGBoost on GOLD and BTC
over a 250-day rolling backtest. No tradable edge found.

**Volatility forecasting (5-day):** EWMA, HAR and Chronos-2 beat Persistence (MAE -19% to -26%).
HAR was best overall; Chronos-2 did not beat HAR.

**Vol-targeting sizing (400 days, costs included, cap 1x):**
- GOLD + EWMA: Sharpe +0.35 vs Buy&Hold (90% bootstrap CI 0.01 to 0.66), lower vol-of-vol, and better than a
  matched constant-exposure control. Borderline evidence: short window, several comparisons, gold was trending up.
- GOLD + HAR: CI includes 0.
- BTC: no benefit (EWMA dSharpe -0.10, CI includes 0; HAR ~ Buy&Hold).

**Correction to Day 4 note:** BTC's lack of effect was NOT due to spike-inflated target vol (median target gave
the same result).Cause (confirmed by clip check): weights hit the 1x cap on 73% (EWMA) and 95% (HAR) of days, so BTC ran as Buy&Hold.

**Caveats:** small samples, multiple comparisons, no live validation. Not trading advice.

**Next:** run `forecast_today.py` regularly and let `results/forecast_log.csv` build an out-of-sample record.
