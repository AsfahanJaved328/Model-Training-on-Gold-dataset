# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-11-05  GOLD 2026-11-04           2.2868        1.5359         1.4617        1.461       1.4866            23.60        -2.576        -4.614             0          0.547
2026-11-05   BTC 2026-11-04           2.0547        1.8486         2.2440        2.151       2.0880            39.89        -3.043        -5.541             1          0.453
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=14)
- mean QLIKE (lower is better): persist 1.853, ewma 0.266, garch 0.276, har 0.265, ens 0.247
- VaR95 violations 2/14 (14.3% vs 5%), binomial p=0.153
- status: monitoring only (need 120 matured forecasts, have 14)
### GOLD (N=9)
- mean QLIKE (lower is better): persist 0.337, ewma 0.352, garch 0.321, har 0.255, ens 0.303
- VaR95 violations 1/9 (11.1% vs 5%), binomial p=0.370
- status: monitoring only (need 120 matured forecasts, have 9)