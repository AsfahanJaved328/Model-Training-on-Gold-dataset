# Final report: Days 13-32

Generated 2026-10-18 19:42 UTC. Rules were fixed before running. Not trading advice.

## Module status
- Day 13: ok
- Day 14: ok
- Day 15: ok
- Day 16: ok
- Day 17: ok
- Day 18: ok
- Day 19: ok
- Day 20: ok
- Day 21: ok
- Day 22: ok
- Day 23: ok
- Day 24: ok
- Day 25: ok
- Day 26: ok
- Day 27: ok
- Day 28: ok
- Day 29: ok
- Day 30: ok

## Findings (auto-generated)
- Day 13: winsorizing returns at 0.1/99.9% changes any strategy Sharpe by at most 0.069 (outliers/roll gaps are not driving results if small).
- Day 14: leakage audit (truncate last 400 days, outputs for earlier dates must be identical): PASS.
- Day 15: false-positive rate of the bootstrap test on pure-noise prices: Trend200 CI_lo>0 0%, p<0.05 16%; VT_EWMA CI_lo>0 5%, p<0.05 8% (nominal: about 5%).
- Day 16 GOLD: lowest QLIKE = GARCH-t; models significantly better than EWMA (one-sided p<0.05, uncorrected): ['GARCH-t', 'Ensemble'].
- Day 16 BTC: lowest QLIKE = Ensemble; models significantly better than EWMA (one-sided p<0.05, uncorrected): ['GARCH-t', 'Ensemble'].
- Day 17: best vol model (lowest QLIKE) across 7 stress windows: Persistence 1, EWMA 1, GARCH-t 2, HAR-cal 2, Ensemble 1
- Day 18 GOLD: QLIKE Chronos-2 0.597 vs EWMA 0.454 vs HAR 0.550 (lower is better).
- Day 18 BTC: QLIKE Chronos-2 1.038 vs EWMA 0.715 vs HAR 0.999 (lower is better).
- Day 19: 0/8 standalone configs PASS (CI_lo>0, >=60% years, dominates buy&hold at equal vol); positive dSharpe in 5/8.
- Day 20: portfolio PASS count 0; dynamic InvVol vs static weights dSharpe -0.082 (CI -0.243..0.094).
- Day 21 GOLD: trend grid (6 variants) median dSharpe -0.132; positive in 0/6; PASS 0/6.
- Day 21 BTC: trend grid (6 variants) median dSharpe 0.142; positive in 6/6; PASS 1/6.
- Day 22: configs with dSharpe>0 at 10 bps: 3/6; at 0 bps: 4/6.
- Day 23: 0/6 strategy-asset pairs beat buy&hold Sharpe in ALL three subperiods (none).
- Day 24: FHS ES ratio (realized tail loss / predicted ES; 1.0 = calibrated) ranges 0.92-1.04; ES residual test p>0.05 in 6/6 cases.
- Day 25 GOLD VaR5%: 9/9 FHS variants pass Kupiec+independence (grid searched, so treat as exploratory).
- Day 25 GOLD VaR1%: 7/9 FHS variants pass Kupiec+independence (grid searched, so treat as exploratory).
- Day 25 BTC VaR5%: 4/9 FHS variants pass Kupiec+independence (grid searched, so treat as exploratory).
- Day 25 BTC VaR1%: 5/9 FHS variants pass Kupiec+independence (grid searched, so treat as exploratory).
- Day 26: Gold-BTC correlation 0.09 (rolling range -0.13..0.30); portfolio FHS VaR: 5% no, 1% PASS.
- Day 27 GOLD: next-day Sharpe in lowest-vol quintile 0.51 vs highest-vol quintile 0.53 (descriptive, no test).
- Day 27 BTC: next-day Sharpe in lowest-vol quintile 1.25 vs highest-vol quintile 1.49 (descriptive, no test).
- Day 28: drawdown-stop rule: GOLD dSharpe -0.101 (CI -0.23..0.03) no; BTC dSharpe -0.062 (CI -0.43..0.34) no.
- Day 29: 40 positive-claim tests this run. Survive Holm (5%): 1; survive BH FDR (5%): 3. Holm survivors: ['D16 BTC Ensemble beats EWMA (QLIKE)'].
- Day 29 caveat: this family covers only Days 13-28; Days 1-12 ran dozens of other tests, so real family-wise error is larger.
- Day 30: unit tests (calibration + no-lookahead + truncation invariance): PASS.

## Tables
### d13_audit
```
Asset    N      Start        End  DupDates  MaxGapDays  ZeroRet%  Robust|z|>8                                                                                  Top5Moves
 GOLD 5478 2005-01-03 2026-10-16         0           5     0.529            5    2026-01-30:-10.8%, 2013-04-15:-9.4%, 2008-09-17:9.0%, 2009-03-19:7.8%, 2006-06-13:-7.3%
  BTC 4400 2014-10-01 2026-10-17         0           1     0.023           12 2020-03-12:-37.2%, 2017-12-07:25.2%, 2017-07-20:23.9%, 2015-01-14:-21.1%, 2017-12-06:19.9%
```

### d13_winsor_sensitivity
```
Asset  BH_orig  VT_orig  Trend_orig  Trend+VT_orig  BH_wins  VT_wins  Trend_wins  Trend+VT_wins
 GOLD    0.658    0.719       0.588          0.691    0.679    0.732       0.582          0.671
  BTC    1.115    1.058       1.161          1.237    1.149    1.127       1.214          1.296
```

### d14_leakage
```
Asset  max|d| features  max|d| HAR walk-fwd  max|d| VT weights  max|d| trend
 GOLD              0.0                  0.0                0.0           0.0
  BTC              0.0                  0.0                0.0           0.0
```

### d15_placebo
```
Strategy  Sims  FP_rate(CI_lo>0)%  FP_rate(p<0.05)%
Trend200   100                0.0              16.0
 VT_EWMA   100                5.0               8.0
```

### d16_vol_horse_race
```
Asset       Model    N  QLIKE  logMAE  Corr(log)  DM_t_vs_EWMA  p_better_than_EWMA
 GOLD Persistence 4907  1.015   0.455      0.377         8.877               1.000
 GOLD      Roll22 4907  0.458   0.371      0.508         4.096               1.000
 GOLD        EWMA 4907  0.421   0.366      0.525           NaN                 NaN
 GOLD     GARCH-t 4907  0.402   0.382      0.530        -2.574               0.005
 GOLD         HAR 4907  0.510   0.346      0.516         4.855               1.000
 GOLD     HAR-cal 4907  0.422   0.383      0.514         0.137               0.555
 GOLD    Ensemble 4907  0.407   0.375      0.527        -2.960               0.002
  BTC Persistence 3829  1.914   0.545      0.457         6.460               1.000
  BTC      Roll22 3829  0.943   0.494      0.486         4.222               1.000
  BTC        EWMA 3829  0.757   0.483      0.515           NaN                 NaN
  BTC     GARCH-t 3829  0.686   0.513      0.508        -2.742               0.003
  BTC         HAR 3829  1.056   0.454      0.487         7.110               1.000
  BTC     HAR-cal 3829  0.708   0.571      0.490        -1.399               0.081
  BTC    Ensemble 3829  0.684   0.520      0.514        -3.045               0.001
```

### d17_vol_by_regime
```
Asset           Regime    N  Persistence  Roll22  EWMA  GARCH-t  HAR-cal  Ensemble
 GOLD Calm(non-stress) 4125        1.018   0.462 0.422    0.398    0.417     0.404
 GOLD              GFC  209        0.538   0.361 0.355    0.399    0.424     0.388
 GOLD             2018  250        1.553   0.450 0.429    0.406    0.401     0.397
 GOLD            COVID   72        0.820   0.959 0.938    1.028    1.263     1.043
 GOLD             2022  251        0.886   0.332 0.314    0.287    0.296     0.295
  BTC Calm(non-stress) 2992        1.896   0.880 0.691    0.637    0.675     0.638
  BTC             2018  365        1.786   1.001 0.658    0.598    0.653     0.606
  BTC            COVID  107        2.637   2.445 2.577    1.943    1.538     1.888
  BTC             2022  365        1.977   0.960 0.868    0.806    0.785     0.787
```

### d18_chronos_vol
```
Asset       Model  N(every 5th day)  QLIKE  logMAE  t_vs_EWMA  p_better_than_EWMA
 GOLD Persistence               982  1.306   0.486      6.269                 1.0
 GOLD        EWMA               982  0.454   0.385        NaN                 NaN
 GOLD         HAR               982  0.550   0.364      3.981                 1.0
 GOLD   Chronos-2               982  0.597   0.379      5.380                 1.0
  BTC Persistence               766  1.810   0.552      5.828                 1.0
  BTC        EWMA               766  0.715   0.483        NaN                 NaN
  BTC         HAR               766  0.999   0.448      5.325                 1.0
  BTC   Chronos-2               766  1.038   0.457      4.152                 1.0
```

### d19_standalone_eqvol
```
Group    Strategy  Sharpe  dSharpe  CI90_lo  CI90_hi  p_boot  YearsWon%  k_eqvol  EqVol_AnnRet%  BH_AnnRet%  EqVol_MaxDD%  BH_MaxDD% VERDICT
 GOLD     VT cap1   0.719    0.060   -0.031    0.157   0.288     47.619    1.267         12.597      12.273       -52.570    -44.364      no
 GOLD     VT cap2   0.679    0.020   -0.114    0.147   0.828     38.095    1.120         12.293      12.273       -55.373    -44.364      no
 GOLD    Trend200   0.588   -0.070   -0.293    0.129   0.514     19.048    1.212         10.332      12.273       -47.648    -44.364      no
 GOLD Trend200+VT   0.691    0.032   -0.203    0.277   0.860     28.571    1.534         11.274      12.273       -54.733    -44.364      no
  BTC     VT cap1   1.058   -0.056   -0.198    0.089   0.490     41.667    1.256         68.255      72.707       -83.532    -83.399      no
  BTC     VT cap2   1.097   -0.017   -0.227    0.186   0.904     41.667    1.060         71.388      72.707       -81.735    -83.399      no
  BTC    Trend200   1.161    0.046   -0.243    0.348   0.774     16.667    1.251         74.960      72.707       -79.394    -83.399      no
  BTC Trend200+VT   1.237    0.123   -0.205    0.470   0.548     33.333    1.639         78.790      72.707       -79.382    -83.399      no
```

### d20_portfolio_eqvol
```
   Group                   Strategy  Sharpe  dSharpe  CI90_lo  CI90_hi  p_boot  YearsWon%  k_eqvol  EqVol_AnnRet%  BH_AnnRet%  EqVol_MaxDD%  BH_MaxDD% VERDICT
GOLD+BTC                     InvVol   1.196   -0.038   -0.317    0.267   0.888     50.000    1.800         38.827      42.532       -50.017    -55.749      no
GOLD+BTC               InvVol+Trend   1.279    0.045   -0.293    0.423   0.788     66.667    2.242         40.350      42.532       -53.733    -55.749      no
GOLD+BTC              Static(0.78G)   1.278    0.044   -0.163    0.264   0.744     50.000    1.692         41.982      42.532       -48.696    -55.749      no
GOLD+BTC InvVol minus Static(0.78G)     NaN   -0.082   -0.243    0.094   0.500        NaN      NaN            NaN         NaN           NaN        NaN     NaN
```

### d21_trend_grid
```
Group Strategy  Sharpe  dSharpe  CI90_lo  CI90_hi  p_boot  YearsWon%  k_eqvol  EqVol_AnnRet%  BH_AnnRet%  EqVol_MaxDD%  BH_MaxDD% VERDICT
 GOLD    SMA50   0.365   -0.293   -0.537   -0.084   0.030     22.727    1.325          5.774      12.159       -59.692    -44.364      no
 GOLD   SMA100   0.505   -0.169   -0.403    0.078   0.288     22.727    1.257          8.593      12.496       -46.368    -44.364      no
 GOLD   SMA150   0.591   -0.077   -0.301    0.145   0.568     18.182    1.230         10.295      12.424       -40.473    -44.364      no
 GOLD   SMA200   0.588   -0.070   -0.284    0.126   0.526     19.048    1.212         10.332      12.273       -47.648    -44.364      no
 GOLD   SMA250   0.515   -0.110   -0.324    0.084   0.370      0.000    1.193          9.032      11.668       -42.355    -44.364      no
 GOLD   MOM252   0.465   -0.154   -0.338    0.040   0.212      9.524    1.154          8.204      11.537       -44.567    -44.364      no
  BTC    SMA50   1.367    0.351    0.031    0.725   0.074     66.667    1.394         88.833      66.904       -72.732    -83.399    PASS
  BTC   SMA100   1.221    0.160   -0.209    0.462   0.502     41.667    1.325         79.554      69.990       -73.573    -83.399      no
  BTC   SMA150   1.360    0.271   -0.035    0.608   0.152     25.000    1.278         87.732      70.933       -71.998    -83.399      no
  BTC   SMA200   1.161    0.046   -0.239    0.370   0.822     16.667    1.251         74.960      72.707       -79.394    -83.399      no
  BTC   SMA250   1.151    0.028   -0.264    0.332   0.850     25.000    1.211         74.762      73.532       -73.828    -83.399      no
  BTC   MOM252   1.243    0.124   -0.150    0.424   0.450     41.667    1.165         80.962      73.352       -78.364    -83.399      no
```

### d22_cost_sensitivity
```
Asset    Strategy  Turn/yr  dSh@0bp  dSh@2bp  dSh@5bp  dSh@10bp  dSh@25bp  dSh@50bp
 GOLD     VT cap1    3.051    0.065    0.060    0.054     0.044     0.013    -0.039
 GOLD    Trend200    7.305   -0.060   -0.070   -0.084    -0.108    -0.180    -0.299
 GOLD Trend200+VT    8.437    0.046    0.032    0.011    -0.023    -0.128    -0.303
  BTC     VT cap1    4.359   -0.048   -0.050   -0.052    -0.056    -0.069    -0.090
  BTC    Trend200    6.518    0.059    0.056    0.052     0.046     0.027    -0.004
  BTC Trend200+VT    8.259    0.143    0.139    0.133     0.123     0.092     0.039
```

### d23_subperiods
```
Asset    Strategy    Period  dSharpe  dMaxDD
 GOLD     VT cap1 2005-2012    0.178   8.424
 GOLD     VT cap1 2012-2019   -0.007   1.149
 GOLD     VT cap1 2019-2026    0.113   6.061
 GOLD    Trend200 2005-2012   -0.105   6.526
 GOLD    Trend200 2012-2019   -0.041  10.903
 GOLD    Trend200 2019-2026   -0.182  -5.044
 GOLD Trend200+VT 2005-2012    0.109  13.697
 GOLD Trend200+VT 2012-2019   -0.060  10.857
 GOLD Trend200+VT 2019-2026   -0.043  -0.492
  BTC     VT cap1 2015-2019    0.020  15.165
  BTC     VT cap1 2019-2022   -0.144   1.804
  BTC     VT cap1 2022-2026   -0.014  -1.292
  BTC    Trend200 2015-2019    0.147  13.276
  BTC    Trend200 2019-2022   -0.029  12.316
  BTC    Trend200 2022-2026   -0.077  21.128
  BTC Trend200+VT 2015-2019    0.382  43.779
  BTC Trend200+VT 2019-2022   -0.019  18.009
  BTC Trend200+VT 2022-2026   -0.067  23.188
```

### d24_es_calibration
```
Asset  Alpha    N  Viol%  Kupiec_p  Indep_p  MeanTailLoss%  PredES%_on_viol  ES_ratio  ES_resid_p
 GOLD  0.050 4976  5.165     0.596    0.498         -2.374           -2.395     0.991       0.976
 GOLD  0.025 4976  2.572     0.745    0.699         -2.793           -2.701     1.034       0.411
 GOLD  0.010 4976  1.125     0.383    0.664         -3.376           -3.243     1.041       0.720
  BTC  0.050 3898  5.259     0.462    0.033         -6.857           -7.219     0.950       0.713
  BTC  0.025 3898  2.668     0.506    0.083         -8.468           -8.906     0.951       0.968
  BTC  0.010 3898  1.231     0.161    0.143         -9.698          -10.564     0.918       0.506
```

### d25_var_grid
```
Asset  Alpha  EWMA_alpha  Window    N  Viol%  Expected%  Kupiec_p  Indep_p VERDICT
 GOLD   0.05        0.03     250 5226  5.243        5.0     0.424    0.498    PASS
 GOLD   0.05        0.03     500 4976  5.105        5.0     0.736    0.774    PASS
 GOLD   0.05        0.03    1000 4476  4.915        5.0     0.794    0.551    PASS
 GOLD   0.05        0.06     250 5226  5.320        5.0     0.294    0.278    PASS
 GOLD   0.05        0.06     500 4976  5.165        5.0     0.596    0.498    PASS
 GOLD   0.05        0.06    1000 4476  4.915        5.0     0.794    0.347    PASS
 GOLD   0.05        0.10     250 5226  5.300        5.0     0.324    0.094    PASS
 GOLD   0.05        0.10     500 4976  5.125        5.0     0.688    0.352    PASS
 GOLD   0.05        0.10    1000 4476  4.982        5.0     0.956    0.303    PASS
 GOLD   0.01        0.03     250 5226  1.206        1.0     0.148    0.048      no
 GOLD   0.01        0.03     500 4976  1.266        1.0     0.070    0.054    PASS
 GOLD   0.01        0.03    1000 4476  1.072        1.0     0.630    0.110    PASS
 GOLD   0.01        0.06     250 5226  1.225        1.0     0.115    0.813    PASS
 GOLD   0.01        0.06     500 4976  1.125        1.0     0.383    0.664    PASS
 GOLD   0.01        0.06    1000 4476  1.139        1.0     0.359    0.614    PASS
 GOLD   0.01        0.10     250 5226  1.397        1.0     0.007    0.984      no
 GOLD   0.01        0.10     500 4976  1.266        1.0     0.070    0.825    PASS
 GOLD   0.01        0.10    1000 4476  1.139        1.0     0.359    0.614    PASS
  BTC   0.05        0.03     250 4148  5.424        5.0     0.216    0.413    PASS
  BTC   0.05        0.03     500 3898  5.208        5.0     0.554    0.099    PASS
  BTC   0.05        0.03    1000 3398  5.091        5.0     0.808    0.453    PASS
  BTC   0.05        0.06     250 4148  5.497        5.0     0.148    0.038      no
  BTC   0.05        0.06     500 3898  5.259        5.0     0.462    0.033      no
  BTC   0.05        0.06    1000 3398  5.062        5.0     0.869    0.652    PASS
  BTC   0.05        0.10     250 4148  5.545        5.0     0.113    0.024      no
  BTC   0.05        0.10     500 3898  5.439        5.0     0.215    0.003      no
  BTC   0.05        0.10    1000 3398  5.062        5.0     0.869    0.018      no
  BTC   0.01        0.03     250 4148  1.350        1.0     0.031    0.227      no
  BTC   0.01        0.03     500 3898  1.206        1.0     0.211    0.020      no
  BTC   0.01        0.03    1000 3398  1.030        1.0     0.861    0.376    PASS
  BTC   0.01        0.06     250 4148  1.398        1.0     0.015    0.258      no
  BTC   0.01        0.06     500 3898  1.231        1.0     0.161    0.143    PASS
  BTC   0.01        0.06    1000 3398  1.001        1.0     0.997    0.353    PASS
  BTC   0.01        0.10     250 4148  1.350        1.0     0.031    0.227      no
  BTC   0.01        0.10     500 3898  1.129        1.0     0.428    0.102    PASS
  BTC   0.01        0.10    1000 3398  1.059        1.0     0.730    0.399    PASS
```

### d26_dependence
```
 Corr(all)  RollCorr250 min  RollCorr250 median  RollCorr250 max  P(Gold<q5 | BTC<q5)%  Gold mean ret% on BTC worst-5% days
     0.095           -0.133               0.079            0.302                 4.225                               -0.064
```

### d26_portfolio_var
```
        Portfolio  Alpha    N  Viol%  Expected%  Kupiec_p  Indep_p VERDICT
50/50 daily-rebal   0.05 2328  5.198        5.0     0.664    0.012      no
50/50 daily-rebal   0.01 2328  1.203        1.0     0.341    0.409    PASS
```

### d27_vol_quintiles
```
Asset  VolQuintile(1=low)    N  AnnRet%  AnnVol%  Sharpe
 GOLD                   1 1179    6.321   12.326   0.513
 GOLD                   2 1095    9.270   15.040   0.617
 GOLD                   3 1114   21.893   15.927   1.375
 GOLD                   4  890    4.521   19.984   0.226
 GOLD                   5  947   15.063   28.207   0.534
  BTC                   1 1073   52.625   42.183   1.248
  BTC                   2  994   40.783   53.151   0.768
  BTC                   3  856   46.843   65.159   0.719
  BTC                   4  634  127.714   77.068   1.658
  BTC                   5  590  145.963   98.303   1.486
```

### d28_dd_stop
```
Group                   Strategy  Sharpe  dSharpe  CI90_lo  CI90_hi  p_boot  YearsWon%  k_eqvol  EqVol_AnnRet%  BH_AnnRet%  EqVol_MaxDD%  BH_MaxDD% VERDICT
 GOLD DD-stop20%/re-enter>SMA200   0.521   -0.101   -0.230    0.029   0.198        0.0    1.079          9.488      11.618       -45.926    -44.364      no
  BTC DD-stop20%/re-enter>SMA200   1.057   -0.062   -0.428    0.338   0.776       25.0    1.360         68.168      73.325       -77.479    -83.399      no
```

### d29_multiple_testing
```
                                   Test     p  Holm_p  BH_q
    D16 BTC Ensemble beats EWMA (QLIKE) 0.001   0.046 0.031
   D16 GOLD Ensemble beats EWMA (QLIKE) 0.002   0.060 0.031
     D16 BTC GARCH-t beats EWMA (QLIKE) 0.003   0.116 0.041
    D16 GOLD GARCH-t beats EWMA (QLIKE) 0.005   0.186 0.050
                           GOLD | SMA50 0.030   1.000 0.240
                            BTC | SMA50 0.074   1.000 0.462
     D16 BTC HAR-cal beats EWMA (QLIKE) 0.081   1.000 0.462
                           BTC | SMA150 0.152   1.000 0.760
      GOLD | DD-stop20%/re-enter>SMA200 0.198   1.000 0.848
                          GOLD | MOM252 0.212   1.000 0.848
                          GOLD | SMA100 0.288   1.000 0.960
                         GOLD | VT cap1 0.288   1.000 0.960
                          GOLD | SMA250 0.370   1.000 1.000
                           BTC | MOM252 0.450   1.000 1.000
                          BTC | VT cap1 0.490   1.000 1.000
            GOLD+BTC | InvVol vs Static 0.500   1.000 1.000
                           BTC | SMA100 0.502   1.000 1.000
                        GOLD | Trend200 0.514   1.000 1.000
                          GOLD | SMA200 0.526   1.000 1.000
                      BTC | Trend200+VT 0.548   1.000 1.000
    D16 GOLD HAR-cal beats EWMA (QLIKE) 0.555   1.000 1.000
                          GOLD | SMA150 0.568   1.000 1.000
               GOLD+BTC | Static(0.78G) 0.744   1.000 1.000
                         BTC | Trend200 0.774   1.000 1.000
       BTC | DD-stop20%/re-enter>SMA200 0.776   1.000 1.000
                GOLD+BTC | InvVol+Trend 0.788   1.000 1.000
                           BTC | SMA200 0.822   1.000 1.000
                         GOLD | VT cap2 0.828   1.000 1.000
                           BTC | SMA250 0.850   1.000 1.000
                     GOLD | Trend200+VT 0.860   1.000 1.000
                      GOLD+BTC | InvVol 0.888   1.000 1.000
                          BTC | VT cap2 0.904   1.000 1.000
     D16 GOLD Roll22 beats EWMA (QLIKE) 1.000   1.000 1.000
   D18 BTC Chronos-2 beats EWMA (QLIKE) 1.000   1.000 1.000
      D16 BTC Roll22 beats EWMA (QLIKE) 1.000   1.000 1.000
        D16 GOLD HAR beats EWMA (QLIKE) 1.000   1.000 1.000
  D18 GOLD Chronos-2 beats EWMA (QLIKE) 1.000   1.000 1.000
 D16 BTC Persistence beats EWMA (QLIKE) 1.000   1.000 1.000
         D16 BTC HAR beats EWMA (QLIKE) 1.000   1.000 1.000
D16 GOLD Persistence beats EWMA (QLIKE) 1.000   1.000 1.000
```
