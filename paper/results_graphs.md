
## Graph Topology and Segregation Differences

To understand how urban design decisions such as the topology of the travel network may
impact the ability for residents to interact (as measured by the segregation index), we
begin with an exploration of correlation among different variables that characterize the
graph topological structure, as well as the correlation between $\Delta_{\tilde{H}}$ and
network structure.

![Clustermap of Correlation Structure in Network Metrics](figures/clustermap.png){#fig:heatmap
width=90%}

@fig:heatmap shows a "clustermap" of the network topology measures, where the
correlation matrix is shaded with green hues to indicate a positive relationship and
purple hues to indicate a negative relationship, with the intensity denoting the level
of correlation. Here, it is clear that some network metrics are capturing the same
concept, for example the gamma index is perfectly collinear with the average node degree
(k_avg) streets per node, and meshedness (given the symmetric nature of the pedestrian
network, the average degree is twice the mean streets per node, since each street flows
both directions). The meshedness index is also highly correlated with the proportion of
four-way intersections, suggesting this component is capturing the network's throughput.

A second group of variables includes population, street length, cyclomatic number,
and measures of street and intersection density. This component appears to measure the
transportation graph's complexity and size. The component may also reveal something
about agglomeration and self scaling, as the density measures appear to grow in tandem
with size. A final third apparent grouping of variables includes circuity, and the
proportion of self loops, as well as three-way and dead-end intersections. This
component is strongly negatively correlated with the first and appears to indicate
network clogging or stoppages. It is interesting to note that circuity is positively
correlated with the proportion of dead-end end streets. Notably each of the three
measures under study (cyclomatic complexity, meshedness, and circuity) each belong to a
different component, suggesting that our chosen variables each represent a distinct part
of the network structure.

![Correlates of $\Delta_{\tilde{H}}$](figures/correlations.png){#fig:correlations width=90%}

@fig:correlations portrays the pairwise correlations between the percentage difference
in the two segregation measures and different properties of the networks in each of the
CBSAs. The strongest correlation is between the percentage difference and the size of
the difference in segregation. This indicates that the percentage differences are not an
artifact of a small denominator problem, whereby low levels of planar segrgation would
result in even small differences between network and planar based segregation to appear
to be large.

Focusing on the network properties, as the proportion of 4-way intersections increases
the difference between segregation measured using network and planar distances grows.
Segregation differences also grow with the average node incidence, street length, edge
length, and circuity of the network. In general, as the size of the network increases,
the difference in the segegation measures decreases. The relative differences in
segregation measures are negatively associated with the level of segregation in the
city.

<!-- I can drop some of the measures such as p-value, but for the ones
to keep, i'm unclear what all the properties are. Maybe these should
be defined above in the methods section and then I can refer to them
here in the narrative -->


Caution about isolating on bivariate relationships and motivate the models that are to come next.




Our two-value test is doing a good job (i.e., it is picking up a difference)

The ps_inter is an interaction term between the planar_measure and whether the two-value test was significant. This tells us that the slope is larger for those cities where the difference in the two-value test is significant.

The pct difference generally declines with the overall level of segregation and network size (as measured by street_length) although the latter association appears to be driven by the places with the significant two-value tests

## Modeling the Difference Between Metrics

To understand the importance of graph structure on the difference between segregation measurements
we also construct a simple regression model using ordinary least squares in which the difference in
segregation is a function of metropolitan network characteristics and population controls,

$$
\Delta_{\tilde{H}} = \alpha + \beta X + \epsilon
$${#eq:diff_model}\
where $\alpha$ is a constant, $X$ is a subset of the variables described in @tbl:variables, and
$\epsilon$ is a vector of random errors. 

<!-- the only change between input is the distance metric, so associations could have a causal interpretation? is that worth it? -->

<!-- this table is ugly. It might be worth doing this in R instead -->
!include tables/regression.md

After removing collinear variables (see @fig:heatmap) such 