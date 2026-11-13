# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-11-12   BTC 2026-11-11           1.2086        1.9908         2.3611       2.1957       2.1878            41.80        -3.253        -5.913             1          0.426
2026-11-13  GOLD 2026-11-12           1.7432        1.5903         1.5039       1.4706       1.5224            24.17        -2.658        -4.760             0          0.555
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=19)
- mean QLIKE (lower is better): persist 1.538, ewma 0.412, garch 0.336, har 0.328, ens 0.331
- VaR95 violations 3/19 (15.8% vs 5%), binomial p=0.067
- status: monitoring only (need 120 matured forecasts, have 19)
### GOLD (N=15)
- mean QLIKE (lower is better): persist 0.542, ewma 0.392, garch 0.371, har 0.307, ens 0.352
- VaR95 violations 2/15 (13.3% vs 5%), binomial p=0.171
- status: monitoring only (need 120 matured forecasts, have 15)