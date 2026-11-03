# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-11-03  GOLD 2026-11-02           1.7756        1.3751          1.333       1.3456       1.3514            21.45        -2.299        -4.252             0          0.549
2026-11-03   BTC 2026-11-02           2.2427        1.6725          2.094       2.0618       1.9522            37.30        -2.734        -4.978             1          0.451
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=12)
- mean QLIKE (lower is better): persist 2.121, ewma 0.281, garch 0.275, har 0.269, ens 0.251
- VaR95 violations 2/12 (16.7% vs 5%), binomial p=0.118
- status: monitoring only (need 120 matured forecasts, have 12)
### GOLD (N=7)
- mean QLIKE (lower is better): persist 0.243, ewma 0.139, garch 0.126, har 0.097, ens 0.116
- VaR95 violations 1/7 (14.3% vs 5%), binomial p=0.302
- status: monitoring only (need 120 matured forecasts, have 7)