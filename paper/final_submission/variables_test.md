\begin{longtable}{l|p{6cm}|c}
\caption{Network Topology Metrics}
\label{tbl:variables}\\
\toprule
               variable &                                                                      description &                                                                                                              formula \\
\midrule
\endfirsthead
\caption[]{Network Topology Metrics} \\
\toprule
               variable &                                                                      description &                                                                                                              formula \\
\midrule
\endhead
\midrule
\multicolumn{3}{r}{{Continued on next page}} \\
\midrule
\endfoot

\bottomrule
\endlastfoot
   Street segments      &                                                Set of street segments in the network &                                                                                                                $E$ \\
   Intersections      &                                                Set of intersections in the network &                                                                                                                $V$ \\
   street-segment-count &                                                Count of street segments in graph &                                                                                                                $n_e = \left | E \right |$ \\
     intersection-count &                                                 Total Intersections in the graph &                                                                                                                $n_v = \left |V \right |$ \\
   streets-per-node-avg &                                                         Average streets per node &                                                                                                    $\frac{n_e}{n_v}$ \\
    street-length-total &                                        Total length (meters) of streets in graph &                                                                                   $\sum_{uv}^E{\operatorname{length}(e_{uv})}$ \\
      street-length-avg &                                                           Average  street length &                                                        $\sum_{uv}^E{\operatorname{length}(e_{uv})}  \left(\frac{1}{n_e}\right)$ \\
      street-density-km &                                                          Street density (per km) &                                                                            $\frac{n_e}{\sum{\operatorname{sqmi}_r}}$ \\
   self-loop-proportion &                      Proportion of edges where node u to node v where u equals v & $  \vert E_{\mathrm{self}} \vert \left( \frac{1}{n_e} \right) ,\;  E_{\mathrm{self}}= \{e\in E \mid e_{uv}=e_{vu}\}$ \\
           circuity-avg &          Ratio of edge lengths to straight-line distances between edge endpoints &                          $\frac{ \sum^E{\operatorname{length}(e_{uv}) }}{\sum^E{\operatorname{distance}(e_u, e_v)}}$ \\
intersection-density-km &                                                       Total Intersections per km &                                                                            $\frac{n_v}{\sum{\operatorname{sqmi}_r}}$ \\
                  k-avg &                                                              Average node degree &                                                                                   $ \sum^V{\deg(v)} (\frac{1}{n_v})$ \\
    node-props-dead-end &                                           Proportion of nodes ending in dead end &                                $ \vert V_2 \vert \left( \frac{ 1}{n_v} \right) ,\;  V_2= \{v\in V \mid \deg(v)=2 \}$ \\
        node-props-3way &                                                Proprotion of 3-way intersections &                                  $ \vert V_3 \vert  \left(\frac{1}{n_v} \right),\;  V_3= \{v\in V \mid \deg(v)=3 \}$ \\
        node-props-4way &                                                Proportion of 4-way intersections &                                 $  \vert V_4 \vert \left(\frac{1 }{n_v} \right),\;  V_4= \{v\in V \mid \deg(v)=4 \}$ \\
             cyclomatic &                                          Number of primary loops in the network. &                                                                                                              $n_e-n_v+1$ \\
             meshedness & Ratio of faces in the network to the max possible loops in an equivalent network &                                                                                                 $\frac{n_e-n_v+1}{2n_v-5}$ \\
                  gamma &                      Number of edges divided divided by 3 times (nodes minus 2)  &                                                                                                  $\frac{n_e}{3(n_v-2)} $ \\
        edge-node-ratio &                                                Ratio of streets to intersections &                                                                                                    $\frac{n_e}{n_v}$ \\
\end{longtable}
