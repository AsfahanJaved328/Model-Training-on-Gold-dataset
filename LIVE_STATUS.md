# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-11-18  GOLD 2026-11-17           1.4078        1.4654         1.4093       1.4403       1.4385            22.84        -2.449        -4.386             0          0.629
2026-11-18   BTC 2026-11-17           3.5280        2.5227         2.8245       2.7135       2.6898            51.39        -4.457        -7.431             0          0.371
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=23)
- mean QLIKE (lower is better): persist 1.643, ewma 0.494, garch 0.354, har 0.369, ens 0.377
- VaR95 violations 5/23 (21.7% vs 5%), binomial p=0.005
- status: monitoring only (need 120 matured forecasts, have 23)
### GOLD (N=18)
- mean QLIKE (lower is better): persist 0.461, ewma 0.332, garch 0.317, har 0.264, ens 0.300
- VaR95 violations 2/18 (11.1% vs 5%), binomial p=0.226
- status: monitoring only (need 120 matured forecasts, have 18)