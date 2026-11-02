# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-10-31  GOLD 2026-10-30           1.6192        1.3437         1.3081       1.3087       1.3203            20.96        -2.242        -4.147             0          0.570
2026-11-02   BTC 2026-10-31           2.0618        1.6782         2.1016       2.0564       1.9546            37.34        -2.744        -4.996             1          0.444
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=10)
- mean QLIKE (lower is better): persist 1.126, ewma 0.259, garch 0.325, har 0.303, ens 0.279
- VaR95 violations 1/10 (10.0% vs 5%), binomial p=0.401
- status: monitoring only (need 120 matured forecasts, have 10)
### GOLD (N=6)
- mean QLIKE (lower is better): persist 0.217, ewma 0.083, garch 0.075, har 0.068, ens 0.071
- VaR95 violations 1/6 (16.7% vs 5%), binomial p=0.265
- status: monitoring only (need 120 matured forecasts, have 6)