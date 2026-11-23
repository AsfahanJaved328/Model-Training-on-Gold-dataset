# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-11-21  GOLD 2026-11-20           2.6759        1.9498         1.8079       1.6117       1.7952            28.50        -3.242        -5.703             0          0.583
2026-11-23   BTC 2026-11-22           3.0400        2.6634         2.9565       2.7992       2.8089            53.66        -4.786        -7.851             0          0.424
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=27)
- mean QLIKE (lower is better): persist 1.415, ewma 0.434, garch 0.305, har 0.322, ens 0.329
- Ensemble better than ewma: one-sided p=0.139 (non-overlapping n=6)
- Ensemble better than persist: one-sided p=0.209 (non-overlapping n=6)
- VaR95 violations 6/27 (22.2% vs 5%), binomial p=0.002
- status: monitoring only (need 120 matured forecasts, have 27)
### GOLD (N=21)
- mean QLIKE (lower is better): persist 0.453, ewma 0.339, garch 0.341, har 0.295, ens 0.321
- VaR95 violations 3/21 (14.3% vs 5%), binomial p=0.085
- status: monitoring only (need 120 matured forecasts, have 21)