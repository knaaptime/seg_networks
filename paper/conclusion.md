<!-- summarize difference result -->

In the segregation literature, the importance of *space* has long been recognized, but a
full grasp of its implications still eludes researchers. In this paper, we show that
when considering the role of transportation infrastructure in segregation measurement,
we obtain substantially different results than classic spatial approaches that adopt
euclidean measurements. More specifically, we show that when ignoring the connectivity
of local travel networks, the spatial information theory index $\tilde{H}$ typically
underestimates four-group racial segregation by approximately 20%. Using a computational
inference framework, we show that this difference is not only substantively meaningful,
but also that the difference is large enough that it is unlikely to result from a random
process. Put differently, we show strong evidence that this bias is prevalent in a large
share of cases. When examining all metropolitan CBSAs in the United States, between 14%
and 25% of the areas show a statistically significant difference, depending on the
$\alpha$ level. This result provides new insight into the importance of considering the
built environment when conducting spatial analysis in general, and measuring
segregation, in particular. By leveraging advances in both network routing algorithms
and statistical methods, we analyze metropolitan regions in the United States at a
massive scale, finding the shortest routes through billions of street intersections to
provide concrete evidence of a widespread phenomenon first suggested by
@roberto2018SpatialProximity.

<!-- summarize graph measures result -->

After demonstrating the importance of considering travel infrastructure in segregation
measurement, we proceed by measuring the topological characteristics of the pedestrian
travel network in each metro region, and assessing their relationships with the observed
differences in segregation. We show that many measures of the graph structure are highly
intercorrelated, and only a few metrics are necessary for capturing a reasonable picture
of the large-scale graph structure. Following, we find that the most important
characteristics in the network are intersection density, which reduces the difference
between network and Euclidean measurements, and the circuity of the street network,
which increases the difference. Critically, the network measures also have significant
interaction effects, showing that the relationship between circuity and segregation
differences is attenuated by the network size, with smaller networks being impacted
less. Together these findings suggest that network design decisions like ensuring dense
and interconnected street grids that adopt straight edges and avoid circuitous patterns
can help reduce the segregation measured in metro regions. Nevertheless, the significant
interaction also suggests more research is necessary to fully understand the effects of
heterogenous network patterns.

<!-- extensions -->

In future work, this research could be extended in several directions. One promising
avenue is the consideration of alternative impedance measures when calculating
shortest-path distances along the travel network. In the present study, we assume a
constant rate of travel consistent with the average walking pace, and that impedance is
reflected by graph distance alone. Alternative constructs could include elevation along
with distance to get a more complete measure of the effort required to traverse by foot
or bicycle. Similarly, the travel network could also be extended to include public
transportation or (potentially congested) automobile travel. These considerations would
require extensive additional data, which may limit the capacity for cross-sectional
comparisons, but would also provide insight into alternative concepts of space and
distance.

Another important avenue for further work is the blending of multiple graphs for a more
complete understanding of multi-contextual segregation. For example children who live in
a given neighborhood are simultaneously embedded in local neighborhood contexts, school
catchment boundaries, and other local institutions such as religious and community
organizations. Each of these contexts have partially-overlapping, occasionally nested,
and often imperfectly-defined geographic boundaries, a full synthesis of which requires
the development of new methods that integrate across these contexts
[@galster2001NatureNeighbourhood;@galster2019making]. As one example,
@wolf2021SpatiallyEncouraged provides a technique for blending multiple graphs together,
one spatial and one aspatial, and similar methods could be possibly used to integrate
multiple contexts. Work along these lines would also help address the call by
@reardon2004MeasuresSpatial [p. 156] for metrics that help understand bridges across
social networks.

An understated but important contribution of this work is its attempt to bridge the gap
between spatial segregation measurement and other areas of spatial analysis. By
formulating a spatial segregation index in terms of a spatial lag operator common in
spatial econometrics, we hope to foster a greater dialog among researchers in urban
social science regarding the most satisfactory ways to encode spatial relationships from
both theoretical and methodological perspectives. Given the results presented here, we
believe the appropriate operationalization of *space* remains a clear hurdle for
understanding social interaction and urban inequality. Thus, we close with a classic
reminder from a legendary scholar in spatial analysis, that "it remains for spatial
analysts to carefully specify spatial weights matrices so that they truly represent the
phenomena being analyzed" [@getis2009SpatialWeights, p.409]. In the context of
segregation measurement, it is clear that ignoring intentionally-designed aspects of the
built-environment skews our concept of social interaction.
