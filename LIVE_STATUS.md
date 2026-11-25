# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-11-25  GOLD 2026-11-24           3.3330        2.1310         1.9964       1.7456       1.9642            31.18        -3.564        -6.269             0          0.544
2026-11-25   BTC 2026-11-24           2.8339        2.5728         2.8916       2.7434       2.7390            52.33        -4.625        -7.586             0          0.456
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=29)
- mean QLIKE (lower is better): persist 1.340, ewma 0.406, garch 0.284, har 0.301, ens 0.306
- Ensemble better than ewma: one-sided p=0.139 (non-overlapping n=6)
- Ensemble better than persist: one-sided p=0.209 (non-overlapping n=6)
- VaR95 violations 7/29 (24.1% vs 5%), binomial p=0.000
- status: monitoring only (need 120 matured forecasts, have 29)
### GOLD (N=23)
- mean QLIKE (lower is better): persist 0.594, ewma 0.501, garch 0.531, har 0.483, ens 0.500
- VaR95 violations 4/23 (17.4% vs 5%), binomial p=0.026
- status: monitoring only (need 120 matured forecasts, have 23)