# Live status v3 (paper tracking, not advice)

## Latest forecasts (daily vol %)

```
  run_date asset  data_date  vol_persist_pct  vol_ewma_pct  vol_garch_pct  vol_har_pct  vol_ens_pct  ens_ann_vol_pct  var95_1d_pct  var99_1d_pct  above_sma200  invvol_weight
2026-10-24   BTC 2026-10-22           1.7149        1.6963         2.1373       2.1455       2.0040            38.29        -2.795        -5.098             1           0.41
2026-10-24  GOLD 2026-10-23           1.1765        1.1891         1.2022       1.2786       1.2239            19.43        -1.992        -3.684             0           0.59
```

## Out-of-sample evaluation (matured forecasts)

### BTC (N=1)
- mean QLIKE (lower is better): persist 0.326, ewma 0.002, garch 0.078, har 0.030, ens 0.023
- VaR95 violations 0/1 (0.0% vs 5%), binomial p=1.000
- status: monitoring only (need 120 matured forecasts, have 1)
### GOLD (N=1)
- mean QLIKE (lower is better): persist 0.024, ewma 0.000, garch 0.001, har 0.011, ens 0.002
- VaR95 violations 0/1 (0.0% vs 5%), binomial p=1.000
- status: monitoring only (need 120 matured forecasts, have 1)