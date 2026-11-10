# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-11-10  GOLD 2026-11-09           1.6913        1.4551         1.3981       1.4221       1.4253            22.63        -2.423        -4.372             0          0.583
2026-11-10   BTC 2026-11-09           2.6758        2.0537         2.4164       2.3636       2.2835            43.63        -3.356        -6.100             1          0.417
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=17)
- mean QLIKE (lower is better): persist 1.587, ewma 0.398, garch 0.288, har 0.288, ens 0.294
- VaR95 violations 3/17 (17.6% vs 5%), binomial p=0.050
- status: monitoring only (need 120 matured forecasts, have 17)
### GOLD (N=12)
- mean QLIKE (lower is better): persist 0.622, ewma 0.454, garch 0.422, har 0.349, ens 0.402
- VaR95 violations 2/12 (16.7% vs 5%), binomial p=0.118
- status: monitoring only (need 120 matured forecasts, have 12)