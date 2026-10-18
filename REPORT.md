# Report: Gold/BTC forecasting & risk toolkit

## Day 8 table
```
   Group        Strategy  AnnRet%  AnnVol%  Sharpe  MaxDD%  VolOfVol  AvgExp  Turn/yr   VERDICT  dSharpe  CI90_lo  CI90_hi  YearsWon%  dMaxDD_vs_BH
    GOLD        Buy&Hold   12.273   18.645   0.658 -44.364     0.436   1.000    0.000         -      NaN      NaN      NaN        NaN           NaN
    GOLD         VT_EWMA   10.572   14.710   0.719 -42.124     0.266   0.876    3.051        no    0.060   -0.030    0.160     47.619         2.239
    GOLD        Trend200    9.051   15.387   0.588 -39.677     0.725   0.688    7.305        no   -0.070   -0.275    0.131     19.048         4.687
    GOLD     Trend200+VT    8.394   12.155   0.691 -36.986     0.622   0.600    8.437        no    0.032   -0.194    0.259     28.571         7.378
     BTC        Buy&Hold   72.707   65.237   1.115 -83.399     0.496   1.000    0.000         -      NaN      NaN      NaN        NaN           NaN
     BTC         VT_EWMA   54.956   51.942   1.058 -74.830     0.370   0.879    4.359        no   -0.056   -0.203    0.088     41.667         8.569
     BTC        Trend200   60.526   52.152   1.161 -70.123     0.937   0.613    6.518 PASS-Risk    0.046   -0.277    0.356     16.667        13.276
     BTC     Trend200+VT   49.240   39.802   1.237 -58.626     0.815   0.531    8.259        no    0.123   -0.211    0.477     33.333        24.773
GOLD+BTC EqualWeight(BH)   42.532   34.465   1.234 -55.749     0.413   1.000    0.000         -      NaN      NaN      NaN        NaN           NaN
GOLD+BTC          InvVol   22.909   19.153   1.196 -30.351     0.389   1.000    0.000        no   -0.038   -0.334    0.299     50.000        25.398
GOLD+BTC    InvVol+Trend   19.662   15.375   1.279 -25.717     0.521   0.688    7.405        no    0.045   -0.323    0.422     66.667        30.033
```

## Day 9 table
```
Asset       Model    N  MAE_logvol  vs_Persist  QLIKE   Corr  p_nonoverlap  YearsBeat% VERDICT
 GOLD Persistence 4907      0.4878      1.0000 1.2899 0.3533           NaN         NaN       -
 GOLD        EWMA 4907      0.3869      0.7932 0.4530 0.5204           0.0       100.0    PASS
 GOLD         HAR 4907      0.3659      0.7501 0.5457 0.5097           0.0       100.0    PASS
  BTC Persistence 3829      0.5633      1.0000 1.9505 0.4321           NaN         NaN       -
  BTC        EWMA 3829      0.4892      0.8685 0.7367 0.5163           0.0       100.0    PASS
  BTC         HAR 3829      0.4547      0.8072 1.0076 0.4960           0.0       100.0    PASS
```

## Day 10 table
```
Asset  Alpha      Method    N  Viol%  Expected%  Kupiec_p  Indep_p VERDICT  Viol%_GFC  Viol%_2018  Viol%_COVID  Viol%_2022
 GOLD   0.05  HistSim500 4976 5.3055        5.0    0.3274   0.2786    PASS     9.5694      3.6000      18.0556      4.7809
 GOLD   0.05 EWMA-Normal 4976 5.2251        5.0    0.4694   0.4451    PASS     4.3062      5.6000       5.5556      6.3745
 GOLD   0.05         FHS 4976 5.1648        5.0    0.5957   0.4985    PASS     3.8278      5.6000       5.5556      5.1793
 GOLD   0.01  HistSim500 4976 1.3666        1.0    0.0138   0.0823      no     2.8708      0.8000       6.9444      0.3984
 GOLD   0.01 EWMA-Normal 4976 2.1704        1.0    0.0000   0.8136      no     0.4785      2.0000       2.7778      2.7888
 GOLD   0.01         FHS 4976 1.1254        1.0    0.3834   0.6641    PASS     0.0000      1.2000       2.7778      0.0000
  BTC   0.05  HistSim500 3898 5.2848        5.0    0.4188   0.0006      no        NaN      5.4795       6.5421      4.1096
  BTC   0.05 EWMA-Normal 3898 4.5921        5.0    0.2364   0.0248      no        NaN      5.7534       5.6075      6.3014
  BTC   0.05         FHS 3898 5.2591        5.0    0.4615   0.0326      no        NaN      5.7534       5.6075      5.2055
  BTC   0.01  HistSim500 3898 1.1288        1.0    0.4285   0.0137      no        NaN      0.8219       0.9346      1.3699
  BTC   0.01 EWMA-Normal 3898 1.8984        1.0    0.0000   0.6299      no        NaN      2.4658       1.8692      2.7397
  BTC   0.01         FHS 3898 1.2314        1.0    0.1611   0.1433    PASS        NaN      1.6438       1.8692      1.6438
```
