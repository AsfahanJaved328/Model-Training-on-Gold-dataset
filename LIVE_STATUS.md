# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-10-28   BTC 2026-10-26           1.5356        1.5194         1.9947       1.8602       1.8026            34.44        -2.503        -4.565             1          0.429
2026-10-28  GOLD 2026-10-27           1.2539        1.1531         1.1740       1.2888       1.2068            19.16        -1.932        -3.575             0          0.571
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=5)
- mean QLIKE (lower is better): persist 1.756, ewma 0.004, garch 0.086, har 0.032, ens 0.026
- VaR95 violations 1/5 (20.0% vs 5%), binomial p=0.226
- status: monitoring only (need 120 matured forecasts, have 5)
### GOLD (N=3)
- mean QLIKE (lower is better): persist 0.044, ewma 0.011, garch 0.005, har 0.005, ens 0.003
- VaR95 violations 0/3 (0.0% vs 5%), binomial p=1.000
- status: monitoring only (need 120 matured forecasts, have 3)