There are two additional parameters worth exploring: the distance-decay function $\phi$, and the
radius that defines the extent of the local environment $r$.

There are also other ways we might partition or conceptualize the street network graph for further
study. In this example, we include a simple set of graph-wide summary measures, e.g. meshedness,
average degree, and circuity. These metrics could also be measured for different subgraphs (e.g.
using the same distance threshold used to define $r$). Summarizing these measures and using them as
input to the regression model would provide a different picture of the relationships; it would also
facilitate the inclusion of other commonly used graph metrics, such as closeness centrality or
betweenness centrality.