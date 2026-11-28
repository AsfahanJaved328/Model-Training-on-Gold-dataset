# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-11-28  GOLD 2026-11-27           3.2189        2.1320         2.0045       1.8142       1.9879            31.56        -3.574        -6.288             0          0.524
2026-11-28   BTC 2026-11-27           1.2720        2.3715         2.7067       2.3188       2.4716            47.22        -4.264        -6.995             0          0.476
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=32)
- mean QLIKE (lower is better): persist 1.275, ewma 0.418, garch 0.321, har 0.324, ens 0.333
- Ensemble better than ewma: one-sided p=0.153 (non-overlapping n=7)
- Ensemble better than persist: one-sided p=0.203 (non-overlapping n=7)
- VaR95 violations 7/32 (21.9% vs 5%), binomial p=0.001
- status: monitoring only (need 120 matured forecasts, have 32)
### GOLD (N=25)
- mean QLIKE (lower is better): persist 0.625, ewma 0.573, garch 0.628, har 0.591, ens 0.592
- VaR95 violations 5/25 (20.0% vs 5%), binomial p=0.007
- status: monitoring only (need 120 matured forecasts, have 25)