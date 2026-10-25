# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-10-24  GOLD 2026-10-23           1.1765        1.1891         1.2022       1.2786       1.2239            19.43        -1.992        -3.684             0          0.590
2026-10-25   BTC 2026-10-23           1.6843        1.6461         2.0926       2.1162       1.9636            37.51        -2.713        -4.947             1          0.417
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=2)
- mean QLIKE (lower is better): persist 0.524, ewma 0.003, garch 0.079, har 0.030, ens 0.023
- VaR95 violations 0/2 (0.0% vs 5%), binomial p=1.000
- status: monitoring only (need 120 matured forecasts, have 2)
### GOLD (N=1)
- mean QLIKE (lower is better): persist 0.024, ewma 0.000, garch 0.001, har 0.011, ens 0.002
- VaR95 violations 0/1 (0.0% vs 5%), binomial p=1.000
- status: monitoring only (need 120 matured forecasts, have 1)