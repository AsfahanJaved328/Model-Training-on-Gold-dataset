# Summary (Days 1-12)

## Earlier findings
- **Price forecasting (1-day):** Naive beat Chronos-Bolt, Chronos-2, Chronos-2+cov and XGBoost on GOLD and BTC. No tradable edge.
- **Vol forecasting (5-day, 2023-26 sample):** EWMA/HAR/Chronos-2 beat Persistence (MAE -19% to -26%); HAR best, Chronos-2 not better than HAR.
- **Vol-targeting, 400 days:** GOLD+EWMA looked borderline positive. **It did not hold on 19.5 years** (dSharpe +0.06, CI includes 0).
  Leverage (1.5x cap) made drawdowns worse. Forecast-based sizing lowered vol-of-vol vs a constant-exposure control in 12/12 configs, at a cost in return.
- **Correction:** BTC's null vol-targeting result was caused by the 1x cap (weights clipped on 73% EWMA / 95% HAR days), not by spike-inflated target vol.

## Day 8 (pre-registered; PASS-Sharpe: CI90_lo>0 and >=60% years beating B&H; PASS-Risk: MaxDD >=10pts shallower and return >=70% of B&H)
Group Strategy  dSharpe  CI90_lo  YearsWon%  dMaxDD_vs_BH   VERDICT
  BTC Trend200    0.046   -0.277     16.667        13.276 PASS-Risk

## Day 9: 5-day vol forecast on long history (PASS: vs Persistence <1, p<0.05 non-overlapping, beats it in >=70% of years)
Asset Model  vs_Persist  p_nonoverlap  YearsBeat%
 GOLD  EWMA      0.7932           0.0       100.0
 GOLD   HAR      0.7501           0.0       100.0
  BTC  EWMA      0.8685           0.0       100.0
  BTC   HAR      0.8072           0.0       100.0

## Day 10: 1-day VaR backtests (PASS: Kupiec p>0.05 and Christoffersen independence p>0.05)
Asset  Alpha      Method  Viol%  Kupiec_p  Indep_p
 GOLD   0.05  HistSim500 5.3055    0.3274   0.2786
 GOLD   0.05 EWMA-Normal 5.2251    0.4694   0.4451
 GOLD   0.05         FHS 5.1648    0.5957   0.4985
 GOLD   0.01         FHS 1.1254    0.3834   0.6641
  BTC   0.01         FHS 1.2314    0.1611   0.1433

## Caveats
GC=F is continuous futures (roll gaps); costs are estimates; many configs tested (8 + 4 + 12); design choices were fixed in advance but are not independent of
the earlier days' results; no live validation yet (see results/forecast_log_v2.csv and forecast_eval.csv, which fill up daily). Not trading advice.
