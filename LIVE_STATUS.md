# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-10-29   BTC 2026-10-27           0.6487        1.4930         1.9704       1.7505       1.7489            33.41        -2.460        -4.486             1          0.428
2026-10-29  GOLD 2026-10-28           1.2767        1.1265         1.1527       1.1936       1.1579            18.38        -1.882        -3.492             0          0.572
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=6)
- mean QLIKE (lower is better): persist 1.644, ewma 0.182, garch 0.317, har 0.274, ens 0.248
- VaR95 violations 1/6 (16.7% vs 5%), binomial p=0.265
- status: monitoring only (need 120 matured forecasts, have 6)
### GOLD (N=4)
- mean QLIKE (lower is better): persist 0.245, ewma 0.022, garch 0.011, har 0.004, ens 0.008
- VaR95 violations 1/4 (25.0% vs 5%), binomial p=0.185
- status: monitoring only (need 120 matured forecasts, have 4)