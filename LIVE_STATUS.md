# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-11-20  GOLD 2026-11-19           1.6417        1.6184         1.5315       1.5079       1.5533            24.66        -2.706        -4.831             0          0.606
2026-11-20   BTC 2026-11-19           1.7722        2.5112         2.8189       2.5491       2.6300            50.25        -4.439        -7.401             0          0.394
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=24)
- mean QLIKE (lower is better): persist 1.577, ewma 0.484, garch 0.342, har 0.361, ens 0.368
- VaR95 violations 6/24 (25.0% vs 5%), binomial p=0.001
- status: monitoring only (need 120 matured forecasts, have 24)
### GOLD (N=20)
- mean QLIKE (lower is better): persist 0.447, ewma 0.310, garch 0.301, har 0.253, ens 0.284
- VaR95 violations 3/20 (15.0% vs 5%), binomial p=0.075
- status: monitoring only (need 120 matured forecasts, have 20)