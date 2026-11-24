# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-11-24  GOLD 2026-11-23           3.1455        2.1067         1.9628       1.7399       1.9423            30.83        -3.525        -6.201             0          0.548
2026-11-24   BTC 2026-11-23           2.7321        2.5823         2.8778       2.7276       2.7319            52.19        -4.640        -7.612             0          0.452
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=28)
- mean QLIKE (lower is better): persist 1.366, ewma 0.419, garch 0.294, har 0.311, ens 0.317
- Ensemble better than ewma: one-sided p=0.139 (non-overlapping n=6)
- Ensemble better than persist: one-sided p=0.209 (non-overlapping n=6)
- VaR95 violations 6/28 (21.4% vs 5%), binomial p=0.002
- status: monitoring only (need 120 matured forecasts, have 28)
### GOLD (N=22)
- mean QLIKE (lower is better): persist 0.490, ewma 0.408, garch 0.425, har 0.383, ens 0.401
- VaR95 violations 3/22 (13.6% vs 5%), binomial p=0.095
- status: monitoring only (need 120 matured forecasts, have 22)