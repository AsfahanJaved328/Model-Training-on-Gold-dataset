# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-11-26  GOLD 2026-11-25           3.0246        2.0740         1.9415       1.7429       1.9243            30.55        -3.468        -6.102             0          0.545
2026-11-27   BTC 2026-11-26           1.4214        2.4317         2.7600       2.4290       2.5450            48.62        -4.372        -7.172             0          0.463
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=31)
- mean QLIKE (lower is better): persist 1.287, ewma 0.408, garch 0.304, har 0.309, ens 0.318
- Ensemble better than ewma: one-sided p=0.153 (non-overlapping n=7)
- Ensemble better than persist: one-sided p=0.203 (non-overlapping n=7)
- VaR95 violations 7/31 (22.6% vs 5%), binomial p=0.001
- status: monitoring only (need 120 matured forecasts, have 31)
### GOLD (N=24)
- mean QLIKE (lower is better): persist 0.589, ewma 0.531, garch 0.573, har 0.530, ens 0.540
- VaR95 violations 4/24 (16.7% vs 5%), binomial p=0.030
- status: monitoring only (need 120 matured forecasts, have 24)