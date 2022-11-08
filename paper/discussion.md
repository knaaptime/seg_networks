There are two additional parameters worth exploring: the distance-decay function $\phi$,
and the radius that defines the extent of the local environment $r$. In this paper we
adopt a simple linear decay function but others such as Gaussian and exponential decay
functions are applied regularly in both the segregation and spatial interaction
literature. Our initial explorations suggest that our findings are robust to the choice
of decay function, but future work could explore this issue in greater detail. Further
work could also explore the choice of neighborhood radius $r$. Here we adopt the
one-mile neighborhood radius as a reasonable specification of the neighborhood, but we
may obtain different results by choosing a different threshold, particularly when
analyzing large heterogeneous networks.

Notably, by varying the $r$ parameter and recalculating the segregation indices
presented here it is possible to generate a network-based version of the "multiscalar
segregation profile" introduced by @reardon2008GeographicScale, which would provide
additional insight into the way that networks may affect multiple scales. In
@fig:multiscalar, we recreate a figure by @roberto2018SpatialProximity showing the
network-based multiscalar profile for Pittsburgh, PA using our data and methodology.
After the critical distance of about one kilometer (which provides travel outside a
given blockgroup) the difference between network and Euclidean profiles is roughly
constant. Again, this initial exploration suggests our results are likely robust to
choice of $r$, but this finding should be subject to further scrutiny.


![Network vs. Eucliden Multiscalar Segregation Profiles for Pittsburgh, PA]()

There are also other ways researchers could partition or conceptualize the street
network graph for further study. In this example, we include a simple set of graph-wide
summary measures, e.g. meshedness, average degree, and circuity. These metrics could
also be measured for different subgraphs (e.g. using the same distance threshold used to
define $r$). Summarizing these measures and using them as input to the regression model
would provide a different picture of the relationships; it would also facilitate the
inclusion of other commonly used graph metrics, such as closeness centrality or
betweenness centrality. The significant interaction effects we uncover between
meshedness and cyclomatic complexity and circuity and complexity also suggest that this
is a ripe avenue for further research. In these cases, the significant interaction
effects are likely created by heterogeneity in large travel networks, and more refined
measures of subgraphs (rather than aggregate summaries of the entire network) may help
uncover important localized patterns.

There is also a second issue of spatial scale, which is that here we examine all
relationships at a metropolitan scale. Because housing and labor markets are regional in
scope, segregation analysis is natural at the metropolitan-level, but adopting such a
large scope may obscure important intra-metropolitan variation. For example,
metropolitan regions have typically been developed over several distinct time periods,
each of which may reflect a particular urban design paradigm or growth management
strategy. Since the network measures computed here are averaged over the entire metro
region, there may be utility in examining how suburban networks differ from urban ones.
Decomposing the urban areas or adopting a multilevel modeling framework could help
examine these nested structures.
