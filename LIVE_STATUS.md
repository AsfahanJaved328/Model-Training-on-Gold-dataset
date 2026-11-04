# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-11-03   BTC 2026-11-02           2.2427        1.6725         2.0940       2.0618       1.9522            37.30        -2.734        -4.978             1          0.451
2026-11-04  GOLD 2026-11-03           1.7614        1.3455         1.3127       1.3452       1.3345            21.19        -2.242        -4.015             0          0.555
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=12)
- mean QLIKE (lower is better): persist 2.121, ewma 0.281, garch 0.275, har 0.269, ens 0.251
- VaR95 violations 2/12 (16.7% vs 5%), binomial p=0.118
- status: monitoring only (need 120 matured forecasts, have 12)
### GOLD (N=8)
- mean QLIKE (lower is better): persist 0.249, ewma 0.182, garch 0.165, har 0.116, ens 0.148
- VaR95 violations 1/8 (12.5% vs 5%), binomial p=0.337
- status: monitoring only (need 120 matured forecasts, have 8)