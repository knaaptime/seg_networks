\begin{table}[h]

\begin{center}
\resizebox{\linewidth}{!}{
\begin{tabular}{lll}
\hline
 variable                & category   & description                                                                                                                             \\
\hline
 streets\_per\_node\_avg    & edge       & average streets per node                                                                                                                \\
 street\_length\_total     & edge       & total length (meters) of streets in graph                                                                                               \\
 street\_segment\_count    & edge       & count of street segments in graph                                                                                                       \\
 street\_length\_avg       & edge       & mean street length                                                                                                                      \\
 street\_density\_km       & edge       & street density (per km)                                                                                                                 \\
 self\_loop\_proportion    & edge       & A self-loop is defined as an edge from node u to node v where u equals v.                                                               \\
 circuity\_avg            & edge       & Sum of edge lengths divided by the sum of straight-line distances between edge endpoints                                                \\
 intersection\_count      & node       & total nodes divided by total intersections                                                                                              \\
 intersection\_density\_km & node       & nodes divided by intersections per km                                                                                                   \\
 node\_props\_dead\_end     & network    & proportion of nodes ending in dead end                                                                                                  \\
 k\_avg                   & network    & average node degree                                                                                                                     \\
 node\_props\_3way         & network    & proprotion of 3-way intersections                                                                                                       \\
 node\_props\_4way         & network    & proportion of 4-way intersections                                                                                                       \\
 cyclomatic              & network    & the number of primary loops in the network. The greater the number of loops, the greater the number of possible routes in the city      \\
 meshedness              & network    & ratio of the number of faces in the network to the maximum possible number of loops in an equivalent network with the same number nodes \\
 edge\_node\_ratio         & network    & ratio of streets to intersections                                                                                                       \\
 gamma                   & network    & number of edges divided divided by 3 times (nodes minus 2)                                                                              \\
\hline
\end{tabular}
}

\caption{Network Topology Metrics}
\label{tbl:tbl:variables}
\end{center}
\end{table}

