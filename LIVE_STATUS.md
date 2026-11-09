# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-11-07  GOLD 2026-11-06           1.8219        1.4808         1.4144       1.4151       1.4371            22.81        -2.466        -4.449             0          0.603
2026-11-09   BTC 2026-11-07           3.1141        2.1380         2.4885       2.4631       2.3686            45.25        -3.493        -6.350             1          0.411
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=16)
- mean QLIKE (lower is better): persist 1.676, ewma 0.401, garch 0.301, har 0.299, ens 0.303
- VaR95 violations 2/16 (12.5% vs 5%), binomial p=0.189
- status: monitoring only (need 120 matured forecasts, have 16)
### GOLD (N=11)
- mean QLIKE (lower is better): persist 0.678, ewma 0.486, garch 0.449, har 0.370, ens 0.428
- VaR95 violations 2/11 (18.2% vs 5%), binomial p=0.102
- status: monitoring only (need 120 matured forecasts, have 11)