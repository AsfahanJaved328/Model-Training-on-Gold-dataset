# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-11-26  GOLD 2026-11-25           3.0246        2.0740         1.9415       1.7429       1.9243            30.55        -3.468        -6.102             0          0.545
2026-11-26   BTC 2026-11-25           1.7211        2.5077         2.8263       2.6078       2.6506            50.64        -4.508        -7.396             0          0.455
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=30)
- mean QLIKE (lower is better): persist 1.307, ewma 0.403, garch 0.290, har 0.300, ens 0.308
- Ensemble better than ewma: one-sided p=0.139 (non-overlapping n=6)
- Ensemble better than persist: one-sided p=0.209 (non-overlapping n=6)
- VaR95 violations 7/30 (23.3% vs 5%), binomial p=0.001
- status: monitoring only (need 120 matured forecasts, have 30)
### GOLD (N=24)
- mean QLIKE (lower is better): persist 0.589, ewma 0.531, garch 0.573, har 0.530, ens 0.540
- VaR95 violations 4/24 (16.7% vs 5%), binomial p=0.030
- status: monitoring only (need 120 matured forecasts, have 24)