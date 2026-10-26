# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-10-24  GOLD 2026-10-23           1.1765        1.1891         1.2022       1.2786       1.2239            19.43        -1.992        -3.684             0          0.590
2026-10-26   BTC 2026-10-24           1.6892        1.5983         2.0585       2.0688       1.9211            36.70        -2.634        -4.803             1          0.424
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=3)
- mean QLIKE (lower is better): persist 1.995, ewma 0.005, garch 0.074, har 0.023, ens 0.019
- VaR95 violations 0/3 (0.0% vs 5%), binomial p=1.000
- status: monitoring only (need 120 matured forecasts, have 3)
### GOLD (N=1)
- mean QLIKE (lower is better): persist 0.024, ewma 0.000, garch 0.001, har 0.011, ens 0.002
- VaR95 violations 0/1 (0.0% vs 5%), binomial p=1.000
- status: monitoring only (need 120 matured forecasts, have 1)