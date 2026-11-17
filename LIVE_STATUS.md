# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-11-17  GOLD 2026-11-16           1.6800        1.5097         1.4422       1.4371       1.4634            23.23        -2.523        -4.519             0           0.63
2026-11-17   BTC 2026-11-16           3.8795        2.6019         2.9094       2.7006       2.7403            52.35        -4.597        -7.664             0           0.37
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=22)
- mean QLIKE (lower is better): persist 1.675, ewma 0.482, garch 0.355, har 0.364, ens 0.372
- VaR95 violations 4/22 (18.2% vs 5%), binomial p=0.022
- status: monitoring only (need 120 matured forecasts, have 22)
### GOLD (N=17)
- mean QLIKE (lower is better): persist 0.479, ewma 0.351, garch 0.336, har 0.279, ens 0.317
- VaR95 violations 2/17 (11.8% vs 5%), binomial p=0.208
- status: monitoring only (need 120 matured forecasts, have 17)