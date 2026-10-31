# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-10-31   BTC 2026-10-29           2.0744        1.7736         2.1795       2.0814       2.0189            38.57        -2.900        -5.280             1           0.43
2026-10-31  GOLD 2026-10-30           1.6192        1.3437         1.3081       1.3087       1.3203            20.96        -2.242        -4.147             0           0.57
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=8)
- mean QLIKE (lower is better): persist 1.366, ewma 0.273, garch 0.406, har 0.375, ens 0.341
- VaR95 violations 1/8 (12.5% vs 5%), binomial p=0.337
- status: monitoring only (need 120 matured forecasts, have 8)
### GOLD (N=6)
- mean QLIKE (lower is better): persist 0.217, ewma 0.083, garch 0.075, har 0.068, ens 0.071
- VaR95 violations 1/6 (16.7% vs 5%), binomial p=0.265
- status: monitoring only (need 120 matured forecasts, have 6)