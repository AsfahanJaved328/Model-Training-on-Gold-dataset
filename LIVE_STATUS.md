# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-11-14  GOLD 2026-11-13           1.6915        1.5419         1.4668       1.4646       1.4915            23.68        -2.577        -4.615             0          0.578
2026-11-15   BTC 2026-11-13           2.7417        2.3271         2.6517       2.4322       2.4740            47.27        -4.104        -6.886             0          0.401
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=20)
- mean QLIKE (lower is better): persist 1.476, ewma 0.392, garch 0.323, har 0.315, ens 0.317
- VaR95 violations 3/20 (15.0% vs 5%), binomial p=0.075
- status: monitoring only (need 120 matured forecasts, have 20)
### GOLD (N=16)
- mean QLIKE (lower is better): persist 0.509, ewma 0.370, garch 0.352, har 0.293, ens 0.333
- VaR95 violations 2/16 (12.5% vs 5%), binomial p=0.189
- status: monitoring only (need 120 matured forecasts, have 16)