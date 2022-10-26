\begin{table}[!htbp] \centering
\begin{tabular}{@{\extracolsep{5pt}}lc}
\\[-1.8ex]\hline
\hline \\[-1.8ex]
& \multicolumn{1}{c}{\textit{Dependent variable:}} \
\cr \cline{1-2}
\\[-1.8ex] & (1) \\
\hline \\[-1.8ex]
 Intercept & -7.730$^{}$ \\
  & (14.149) \\
 circuity\_avg & -0.015$^{}$ \\
  & (0.018) \\
 meshedness & -2.141$^{**}$ \\
  & (0.952) \\
 node\_props\_3way & 3.930$^{}$ \\
  & (5.913) \\
 node\_props\_4way & 2.770$^{}$ \\
  & (3.203) \\
 node\_props\_dead\_end & 5.189$^{}$ \\
  & (11.562) \\
 np.log(ALAND) & -0.000$^{}$ \\
  & (0.003) \\
 np.log(AWATER) & -0.001$^{}$ \\
  & (0.001) \\
 np.log(cyclomatic) & 0.359$^{}$ \\
  & (0.268) \\
 np.log(intersection\_density\_km) & -0.983$^{}$ \\
  & (0.722) \\
 np.log(pop\_density) & 0.001$^{}$ \\
  & (0.002) \\
 np.log(population) & 0.001$^{}$ \\
  & (0.002) \\
 np.log(street\_density\_km) & 0.979$^{}$ \\
  & (0.722) \\
 np.log(street\_length\_avg) & -0.540$^{}$ \\
  & (0.449) \\
 np.log(street\_length\_total) & -0.449$^{}$ \\
  & (0.291) \\
 np.log(street\_segment\_count) & 0.091$^{}$ \\
  & (0.228) \\
 planar\_measure & 0.005$^{}$ \\
  & (0.009) \\
 self\_loop\_proportion & -0.050$^{}$ \\
  & (0.221) \\
 streets\_per\_node\_avg & 1.856$^{}$ \\
  & (2.753) \\
\hline \\[-1.8ex]
 Observations & 369 \\
 $R^2$ & 0.110 \\
 Adjusted $R^2$ & 0.069 \\
 Residual Std. Error & 0.011(df = 352)  \\
 F Statistic & 2.717$^{***}$ (df = 16.0; 352.0) \\
\hline
\hline \\[-1.8ex]
\textit{Note:} & \multicolumn{1}{r}{$^{*}$p$<$0.1; $^{**}$p$<$0.05; $^{***}$p$<$0.01} \\
\end{tabular}
\end{table}