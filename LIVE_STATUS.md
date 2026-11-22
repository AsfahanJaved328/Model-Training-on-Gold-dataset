# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-11-21  GOLD 2026-11-20           2.6759        1.9498         1.8079       1.6117       1.7952            28.50        -3.242        -5.703             0          0.583
2026-11-22   BTC 2026-11-21           2.9363        2.7108         2.9959       2.7422       2.8192            53.86        -4.868        -7.985             0          0.420
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=26)
- mean QLIKE (lower is better): persist 1.468, ewma 0.448, garch 0.317, har 0.334, ens 0.340
- Ensemble better than ewma: one-sided p=0.139 (non-overlapping n=6)
- Ensemble better than persist: one-sided p=0.209 (non-overlapping n=6)
- VaR95 violations 6/26 (23.1% vs 5%), binomial p=0.002
- status: monitoring only (need 120 matured forecasts, have 26)
### GOLD (N=21)
- mean QLIKE (lower is better): persist 0.453, ewma 0.339, garch 0.341, har 0.295, ens 0.321
- VaR95 violations 3/21 (14.3% vs 5%), binomial p=0.085
- status: monitoring only (need 120 matured forecasts, have 21)