# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-10-30   BTC 2026-10-28           0.6847        1.4543         1.9382       1.7677       1.7317            33.08        -2.396        -4.370             1          0.428
2026-10-30  GOLD 2026-10-29           0.8526        1.0991         1.1304       1.1833       1.1381            18.07        -1.836        -3.407             0          0.572
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=7)
- mean QLIKE (lower is better): persist 1.547, ewma 0.288, garch 0.464, har 0.429, ens 0.388
- VaR95 violations 1/7 (14.3% vs 5%), binomial p=0.302
- status: monitoring only (need 120 matured forecasts, have 7)
### GOLD (N=5)
- mean QLIKE (lower is better): persist 0.209, ewma 0.053, garch 0.046, har 0.056, ens 0.047
- VaR95 violations 1/5 (20.0% vs 5%), binomial p=0.226
- status: monitoring only (need 120 matured forecasts, have 5)