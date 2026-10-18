# Summary (Days 1-7)

**Price forecasting (1-day):** Naive beat Chronos-Bolt, Chronos-2, Chronos-2+cov and XGBoost on GOLD and BTC
(250-day rolling backtest). No tradable edge.

**Volatility forecasting (5-day):** EWMA, HAR and Chronos-2 beat Persistence (MAE -19% to -26%); HAR best, Chronos-2 not better than HAR.

**Vol-targeting (Day 4-5, 400 days):** GOLD+EWMA borderline positive; BTC no effect. Correction: BTC's null result was caused by the
1x cap (weights clipped at 1 on 73% EWMA / 95% HAR days), not by spike-inflated target vol.

**Day 7 long-history test** (Gold from 2005, BTC from 2014; expanding walk-forward; caps 1.0 and 1.5; financing and costs included).
Pass rule fixed before running: CI90_lo>0 AND beat Buy&Hold in >=60% of years AND better MaxDD.

No configuration passed the pre-registered rule (CI90_lo>0, YearsWon>=60%, MaxDD better than Buy&Hold).

Full table: results/metrics_day7_longhistory.csv ; per-year: results/metrics_day7_yearly.csv

**Caveats:** GC=F is continuous futures (roll gaps), cost assumptions are estimates, 12 configs tested per asset set, no live validation. Not trading advice.
