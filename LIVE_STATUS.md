# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-10-27   BTC 2026-10-25           1.6392        1.5671         2.0357       2.0135       1.8845            36.00        -2.582        -4.709             1          0.425
2026-10-27  GOLD 2026-10-26           1.2035        1.1678         1.1867       1.2786       1.2120            19.24        -1.956        -3.619             0          0.575
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=4)
- mean QLIKE (lower is better): persist 1.985, ewma 0.005, garch 0.076, har 0.024, ens 0.020
- VaR95 violations 0/4 (0.0% vs 5%), binomial p=1.000
- status: monitoring only (need 120 matured forecasts, have 4)
### GOLD (N=2)
- mean QLIKE (lower is better): persist 0.033, ewma 0.002, garch 0.001, har 0.008, ens 0.001
- VaR95 violations 0/2 (0.0% vs 5%), binomial p=1.000
- status: monitoring only (need 120 matured forecasts, have 2)