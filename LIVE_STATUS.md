# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-11-21  GOLD 2026-11-20           2.6759        1.9498         1.8079       1.6117       1.7952            28.50        -3.242        -5.703             0          0.583
2026-11-21   BTC 2026-11-20           2.7871        2.7412         3.0281       2.6143       2.7999            53.49        -4.916        -8.065             0          0.417
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=25)
- mean QLIKE (lower is better): persist 1.521, ewma 0.465, garch 0.329, har 0.347, ens 0.353
- VaR95 violations 6/25 (24.0% vs 5%), binomial p=0.001
- status: monitoring only (need 120 matured forecasts, have 25)
### GOLD (N=21)
- mean QLIKE (lower is better): persist 0.453, ewma 0.339, garch 0.341, har 0.295, ens 0.321
- VaR95 violations 3/21 (14.3% vs 5%), binomial p=0.085
- status: monitoring only (need 120 matured forecasts, have 21)