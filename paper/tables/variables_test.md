\begin{longtable}{l|p{6cm}|l}
\caption{Network Topology Metrics}
\label{tbl:variables}\\
\toprule
               variable &                                                                      description &                                                                         formula \\
\midrule
\endfirsthead
\caption[]{Network Topology Metrics} \\
\toprule
               variable &                                                                      description &                                                                         formula \\
\midrule
\endhead
\midrule
\multicolumn{3}{r}{{Continued on next page}} \\
\midrule
\endfoot

\bottomrule
\endlastfoot
   streets-per-node-avg &                                                         Average streets per node &                                                               $\frac{n_e}{n_v}$ \\
    street-length-total &                                        Total length (meters) of streets in graph &                                                    $\sum^E{\mathbf{length}(e)}$ \\
   street-segment-count &                                                Count of street segments in graph &                                                                           $n_e$ \\
      street-length-avg &                                                           Average  street length &                                         $\frac{\sum^e{\mathbf{length}_e}}{n_e}$ \\
      street-density-km &                                                          Street density (per km) &                                             $\frac{n_e}{\sum{\mathbf{sqmi}_r}}$ \\
   self-loop-proportion &                      Proportion of edges where node u to node v where u equals v &  $\frac{ \vert E_{self} \vert }{n_e},  E_{self}= \{e\in r \mid e_{uv}=e_{vu}\}$ \\
           circuity-avg &          Ratio of edge lengths to straight-line distances between edge endpoints & $\frac{ \sum^E{\mathbf{length}(e_{uv}) }}{\sum^E{\mathbf{distance}(e_u, e_v)}}$ \\
     intersection-count &                                                 Total Intersections in the graph &                                                                           $n_v$ \\
intersection-density-km &                                                       Total Intersections per km &                                             $\frac{n_v}{\sum{\mathbf{sqmi}_r}}$ \\
    node-props-dead-end &                                           Proportion of nodes ending in dead end &    $\frac{ \vert V_1 \vert }{n_v},  V_1= \{v\in r \mid \mathbf{degree}(v)=1 \}$ \\
                  k-avg &                                                              Average node degree &                                      $\frac{\sum^V{\mathbf{degree}(v)}  }{n_v}$ \\
        node-props-3way &                                                Proprotion of 3-way intersections &  $\frac{ \vert V_3 \ \vert }{n_v},  V_3= \{v\in r \mid \mathbf{degree}(v)=3 \}$ \\
        node-props-4way &                                                Proportion of 4-way intersections &    $\frac{ \vert V_4 \vert }{n_v},  V_4= \{v\in r \mid \mathbf{degree}(v)=4 \}$ \\
             cyclomatic &                                          Number of primary loops in the network. &                                                                         $e-v+1$ \\
             meshedness & Ratio of faces in the network to the max possible loops in an equivalent network &                                                            $\frac{e-v+1}{2v-5}$ \\
        edge-node-ratio &                                                Ratio of streets to intersections &                                                               $\frac{n_e}{n_v}$ \\
                  gamma &                      Number of edges divided divided by 3 times (nodes minus 2)  &                                                             $\frac{e}{3(v-2)} $ \\
\end{longtable}
