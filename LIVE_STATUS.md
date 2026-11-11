# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-11-10   BTC 2026-11-09           2.6758        2.0537         2.4164       2.3636       2.2835            43.63        -3.356        -6.100             1          0.417
2026-11-11  GOLD 2026-11-10           1.8996        1.4992         1.4324       1.4333       1.4553            23.10        -2.494        -4.499             0          0.576
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=17)
- mean QLIKE (lower is better): persist 1.587, ewma 0.398, garch 0.288, har 0.288, ens 0.294
- VaR95 violations 3/17 (17.6% vs 5%), binomial p=0.050
- status: monitoring only (need 120 matured forecasts, have 17)
### GOLD (N=13)
- mean QLIKE (lower is better): persist 0.575, ewma 0.443, garch 0.417, har 0.345, ens 0.396
- VaR95 violations 2/13 (15.4% vs 5%), binomial p=0.135
- status: monitoring only (need 120 matured forecasts, have 13)