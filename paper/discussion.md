There are two additional parameters worth exploring: the distance-decay function $\phi$, and the
radius that defines the extent of the local environment $r$.

There are also other ways we might partition or conceptualize the street network graph for further
study. In this example, we include a simple set of graph-wide summary measures, e.g. meshedness,
average degree, and circuity. These metrics could also be measured for different subgraphs (e.g.
using the same distance threshold used to define $r$). Summarizing these measures and using them as
input to the regression model would provide a different picture of the relationships; it would also
facilitate the inclusion of other commonly used graph metrics, such as closeness centrality or
betweenness centrality.

There is also a second issue of spatial scale, which is that we're examining all of these trends at a metropolitan scale. Because housing and labor markets are regional in scope, segregation analysis is natural at the metropolitan-level, but adopting such a large scope may obscure important intra-metropolitan variation. For example, metropolitan regions have typically been developed over several distinct time periods, each of which may reflect a particular urban design paradigm or growth management strategy. Since the network measures computed here are averaged over the entire metro region, there may be utility in examining how suburban networks differ from urban ones. Decomposing the urban areas or adopting a multilevel modeling framework could help 

In many cases, there are important