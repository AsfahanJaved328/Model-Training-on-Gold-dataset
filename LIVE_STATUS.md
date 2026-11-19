# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-11-19  GOLD 2026-11-18           1.9853        1.6246         1.5335       1.5087       1.5564            24.71        -2.717        -4.849             0          0.608
2026-11-19   BTC 2026-11-18           3.2086        2.5526         2.8632       2.7038       2.7095            51.77        -4.511        -7.521             0          0.392
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=24)
- mean QLIKE (lower is better): persist 1.577, ewma 0.484, garch 0.342, har 0.361, ens 0.368
- VaR95 violations 6/24 (25.0% vs 5%), binomial p=0.001
- status: monitoring only (need 120 matured forecasts, have 24)
### GOLD (N=19)
- mean QLIKE (lower is better): persist 0.470, ewma 0.326, garch 0.316, har 0.265, ens 0.298
- VaR95 violations 3/19 (15.8% vs 5%), binomial p=0.067
- status: monitoring only (need 120 matured forecasts, have 19)