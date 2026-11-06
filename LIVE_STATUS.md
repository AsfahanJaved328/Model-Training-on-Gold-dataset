# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-11-06  GOLD 2026-11-05           2.3185        1.5087         1.4342       1.4628       1.4689            23.32        -2.531        -4.533             0          0.599
2026-11-06   BTC 2026-11-05           3.2750        2.2736         2.6237       2.4766       2.4621            47.04        -3.715        -6.752             1          0.401
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=15)
- mean QLIKE (lower is better): persist 1.769, ewma 0.346, garch 0.294, har 0.288, ens 0.282
- VaR95 violations 2/15 (13.3% vs 5%), binomial p=0.171
- status: monitoring only (need 120 matured forecasts, have 15)
### GOLD (N=10)
- mean QLIKE (lower is better): persist 0.743, ewma 0.512, garch 0.466, har 0.379, ens 0.445
- VaR95 violations 2/10 (20.0% vs 5%), binomial p=0.086
- status: monitoring only (need 120 matured forecasts, have 10)