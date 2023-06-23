
## Graph Topology and Segregation Differences

We begin with an exploration of correlation among different variables that characterize
the graph topological structure, as well as the correlation between $\Delta_{\tilde{H}}$
and network structure. @fig:heatmap shows a "clustermap" of the network topology
measures, where the correlation matrix is shaded with green hues indicating positive
relationships with purple hues indicating negative relationships, and the intensity
denoting the level of correlation. Some network metrics clearly capture the same
concept; for example the gamma index is perfectly collinear with the average node degree
(k_avg), streets per node, and meshedness (given the symmetric nature of the pedestrian
network, the average degree is twice the mean streets per node, since each street flows
both directions). The meshedness index is also highly correlated with the proportion of
four-way intersections, suggesting this component is capturing the network's throughput.

![Clustermap of Correlation Structure in Network Metrics](figures/clustermap.png){#fig:heatmap
width=90%}

A second group of variables includes population, street length, cyclomatic number,
and measures of street and intersection density. This component appears to measure the
transportation graph's complexity and size. The component may also reveal something
about agglomeration and self-scaling, as the density measures appear to grow in tandem
with size. A final third apparent grouping of variables includes circuity, and the
proportion of self-loops, as well as three-way and dead-end intersections. This
component is strongly negatively correlated with the first and appears to indicate
network clogging or stoppages. It is interesting to note that circuity is positively
correlated with the proportion of dead-end end streets. Notably each of the three
measures under study (cyclomatic complexity, meshedness, and circuity) each belong to a
different component, suggesting that our chosen variables each represent a distinct part
of the network structure.

@fig:correlations in the supplementary material portrays the pairwise correlations
between the percentage difference in the two segregation measures and different
properties of the networks in each of the CBSAs. The strongest correlation is between
the percentage difference and the size of the difference in segregation. This indicates
that the percentage differences are not an artifact of a small denominator problem,
whereby low levels of planar segregation would result in even small differences between
network and planar based segregation to appear to be large. Focusing on the network
properties, as the proportion of 4-way intersections increases the difference between
segregation measured using network and planar distances grows. Segregation differences
also grow with the average node incidence, street length, edge length, and circuity of
the network. In general, as the size of the network increases, the difference in the
segregation measures decreases. The relative differences in segregation measures are
negatively associated with the level of segregation in the city.

<!-- I can drop some of the measures such as p-value, but for the ones
to keep, i'm unclear what all the properties are. Maybe these should
be defined above in the methods section and then I can refer to them
here in the narrative 

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
-->

## Modeling the Difference Between Metrics

To understand the importance of graph structure on the difference between segregation
measurements we also fit a series of regression models where the difference in
segregation is a function of metropolitan network characteristics and population
controls. Two models are presented, where the dependent variable $\Delta$ is either the
observed difference between segregation measures, or the percent difference between the
two:

<!--
Because distance computation is the only systematic difference between the
Euclidean and network-based segregation measures, we can reasonably interpret the
coefficients from the regression as the "effects" of different network structure on the
difference between measures, given the usual caveats about potential omitted variable
bias. Note this does not suggest a causal interpretation of the effects of network
structure on *segregation*, per se, but rather the effect of network configuration on
the *calculation of the segregation index*.
-->

$$
\Delta = \alpha + \beta X + \epsilon
$${#eq:diff_model}\
where $\alpha$ is a constant, $X$ is a subset of the variables described in @tbl:variables, and
$\epsilon$ is a vector of random errors. 

!include tables/regression.md

After removing collinear variables such as the share of proportions in different
connectivity levels and other constructs well-captured by other variables (see
@fig:heatmap), our preferred models include a subset of network topology measures and
interactions between cyclomatic complexity and (1) meshedness (2) circuity. In all
specifications, these interactions significantly improved model fit. Moreover, the
relationships between variables are generally consistent regardless which dependent
variable is used. Right-hand side variables following a Normal distribution are
z-transformed and those following a power distribution are transformed via natural
logarithm.

Regardless of the chosen dependent variable, the models display similar results, most of
which are intuitive. Significant variables include the density of streets and street
intersections, network circuity, and the two interaction terms. As expected, the
coefficient for intersection density is negative, suggesting that as the number of
intersections per kilometer increases the gap between Euclidean and network-based
segregation indices falls. This comports with intuition as greater intersection density
leads to a network with greater ability to change direction, and thus a better
approximation of unconstrained travel. Circuity is also positive and significant,
suggesting that as streets get more winding and curvilinear, the distance between
segregation indices grows. However, the interaction between cyclomatic complexity (a
measure of redundancy in the network) and circuity is negative, which suggests that as
the network offers more possible routes between an origin and destination, the effect of
circuity falls. Again, this result is intuitive, as increased cyclomatic complexity
offers more opportunities for short-cutting through a circuitous network.

One counterintuitive result is the weakly significant and positive coefficient for
network meshedness. Taken at face value, this would suggest that networks with a regular
grid pattern increase the distance between segregation measured on the network versus
the same data measured on a plane. One possible explanation for this result is an
inability of this relatively simple model to account for multiple interactions between
meshedness, density, and complexity. While it is possible for a street network to have
high intersection density, high street density, and low meshedness (such as a dense but
highly dendritic subdivision) such networks are likely comparatively rare in major
cities (or are difficult to capture at a metropolitan scale). In such a situation, some
variation attributable to meshedness may instead be consumed by the competing
coefficients for street density and network density. Exploring the complexity of these
relationships is an important avenue for further work.
