# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-11-12  GOLD 2026-11-11           1.2358        1.4647         1.4073       1.4143       1.4290            22.69        -2.437        -4.396             0          0.574
2026-11-12   BTC 2026-11-11           1.2086        1.9908         2.3611       2.1957       2.1878            41.80        -3.253        -5.913             1          0.426
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=19)
- mean QLIKE (lower is better): persist 1.538, ewma 0.412, garch 0.336, har 0.328, ens 0.331
- VaR95 violations 3/19 (15.8% vs 5%), binomial p=0.067
- status: monitoring only (need 120 matured forecasts, have 19)
### GOLD (N=14)
- mean QLIKE (lower is better): persist 0.571, ewma 0.417, garch 0.391, har 0.324, ens 0.372
- VaR95 violations 2/14 (14.3% vs 5%), binomial p=0.153
- status: monitoring only (need 120 matured forecasts, have 14)