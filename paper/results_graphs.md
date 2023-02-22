
## Graph Topology and Segregation Differences

To understand how urban design decisions such as the topology of the travel network may
impact the ability for residents to interact (as measured by the segregation index), we
begin with an exploration of correlation among different variables that characterize the
graph topological structure, as well as the correlation between $\Delta_{\tilde{H}}$ and
network structure. @fig:heatmap shows a "clustermap" of the network topology measures,
where the correlation matrix is shaded with green hues to indicate a positive
relationship and purple hues to indicate a negative relationship, with the intensity
denoting the level of correlation. Here, it is clear that some network metrics are
capturing the same concept, for example the gamma index is perfectly collinear with the
average node degree (k_avg) streets per node, and meshedness (given the symmetric nature
of the pedestrian network, the average degree is twice the mean streets per node, since
each street flows both directions). The meshedness index is also highly correlated with
the proportion of four-way intersections, suggesting this component is capturing the
network's throughput.

![Clustermap of Correlation Structure in Network Metrics](figures/clustermap.png){#fig:heatmap
width=90%}

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
artifact of a small denominator problem, whereby low levels of planar segregation would
result in even small differences between network and planar based segregation to appear
to be large. Focusing on the network properties, as the proportion of 4-way
intersections increases the difference between segregation measured using network and
planar distances grows. Segregation differences also grow with the average node
incidence, street length, edge length, and circuity of the network. In general, as the
size of the network increases, the difference in the segregation measures decreases. The
relative differences in segregation measures are negatively associated with the level of
segregation in the city.

<!-- I can drop some of the measures such as p-value, but for the ones
to keep, i'm unclear what all the properties are. Maybe these should
be defined above in the methods section and then I can refer to them
here in the narrative -->

Our results demonstrate that the two-value test presented in the previous section is
performing well by distinguishing a real difference between the two measurement
techniques. The variable $ps\_inter$ is an interaction term between the planar_measure
and whether the two-value test was significant. These results show that the slope is
larger for those cities where the difference in the two-value test is significant. We
also find that the percent difference generally declines with the overall level of
segregation and network size (as measured by street_length) although the latter
association appears to be driven by the places with the significant two-value tests.
While informative, these bivariate associations can be difficult to interpret, given the
strong intercorrelation structure of many variables of interest, and therefore must be
interpreted with caution. As such, we attempt to isolate the relationships among
variables in the following section.

## Modeling the Difference Between Metrics

To understand the importance of graph structure on the difference between segregation
measurements we also fit a series of regression models in which the difference in
segregation is a function of metropolitan network characteristics and population
controls. We fit both frequentist and Bayesian model specifications, with the latter
adopting weakly-informative priors using both the raw difference in segregation and the
percent difference as the dependent variable [@capretto2022BambiSimple].

$$
\Delta = \alpha + \beta X + \epsilon
$${#eq:diff_model}\
where $\alpha$ is a constant, $X$ is a subset of the variables described in @tbl:variables, and
$\epsilon$ is a vector of random errors. 

<!-- the only change between input is the distance metric, so associations could have a causal interpretation? is that worth it? -->

<!-- this table is ugly. It might be worth doing this in R instead -->
!include tables/regression.md

By adopting this full array of model specifications, we aim to provide as much insight into
the data as possible and leverage the best metrics from both approaches; diagnostics
from the frequentist models provide an overview of how much variance each model explains
via familiar metrics like the $R^2$ statistic, whereas the Bayesian models provide
extremely useful uncertainty estimates of other parameters. After removing collinear
variables such as the share of proportions in different connectivity levels and other
constructs well-captured by other variables (see @fig:heatmap), our preferred models
include a subset of network topology measures and interactions between cyclomatic
complexity and (1) meshedness (2) circuity. In all specifications, these interactions
improved model fit significantly. Our Bayesian and frequentist specifications provide
complimentary results and the relationships between variables are generally consistent
regardless which dependent variable is used.

