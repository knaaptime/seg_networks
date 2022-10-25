We begin our analysis by computing two sets of segregation indices, adopting the spatial information
theory index $\tilde{H}$ as our measure of segregation. As @reardon2008GeographicScale [p. 512]
describe, "the index $\tilde{H}$ is a measure of how much less diverse individuals’ local
environments are, on average, than is the total population of region", and reaches its maximum of 1
only when "each individual's local environment is monoracial". Here, our goal is to test how
sensitive the statistic is to different concepts of the "local environment," with one concept
adopting the simplified assumption of euclidean-based distance measurements, and the other requiring
that distance be measured along a pedestrian transport network.

## Measuring Segregation in Space

<!-- computing indices -->

Following @reardon2004MeasuresSpatial we consider a spatial region $R$ populated by $M$ racial
groups indexed by $m$, with $\tau$ and $\pi$ as population density and proportion, respectively.
Here we diverge from the classical notation in the segregation literature and instead adopt
conventions more common in spatial econometrics and geographic analysis. Doing so allows us to
strengthen the connection between similar concepts in different disciplines as well as gain finer
control over the definition of spatial relationships. Since many spatial segregation measures are
implemented in GIS and spatial analysis software designed by geographers, clarifying this connection
can help ease interdisciplinary adoption and conversation around spatial segregation measures.

Thus, we index locations within $R$ as $i$ and $j$, and we operationalize the concept of spatial
relationships using a spatial weights matrix $W_{ij}$. By focusing on $W_{ij}$, we are forced "to
specify [our] underlying assumptions about socio-spatial proximity", following the call by
@reardon2004MeasuresSpatial [p.154] for analysis that "compares segregation levels based on
different theoretical bases for defining spatial proximity." Conceptually, the spatial weights
matrix $W_{ij}$ is connectivity graph that defines the spatial relationship between nodes $i$ and
$j$, and the values $w_{ij}$ encode the intensity of the edge $\bar{ij}$. Thus, the spatial weights
matrix is a useful and flexible representation of the local neighborhood environment because it
provides a generic data structure for encoding spatial relationships, where any link function
($\phi$, following the notation of @reardon2004MeasuresSpatial) can be used to specify the proximity
between units. Formally,

<!-- if we're following reardon's notation, does $D$ below need to be $R$ ? -->
$$
W_{ij} = \phi(D_{ij})
$$ {#eq:weights}\
Where $\phi$ is a proximity weighting function and $D$ is a matrix containing pairwise distances for
$i$ and $j$. Classically, $W_{ij}$ is typically created via binary connectivity between adjacent
units, but a wide variety of other continuous specifications are also used in practice
[@getis2009SpatialWeights;@rey2010PySALPython;@halleckvega2015SLXMODEL], such as the euclidean
distance between observations, or various kernel or distance-decay functions. Critically, the
distance-weighting function $\phi$ is distinct from the concept of *distance* ($D$), itself, which
could be measured in Euclidean/geodesic distance, minutes of congested travel time, meters traveled
along the sidewalk, or some generalized measure of utility. Separating these two concepts allows us
to consider alternative distance metrics distinctly from alternative decay functions. The local
environment for a given feature $y$ at location $i$ can then be measured by its *spatial lag*, $SL$,
defined as

$$
SL_i = \sum_j w_{ij} y_j
$$ {#eq:lag}\
In the spatial econometrics literature, it is common to exclude the diagonal elements from $W_{ij}$
to differentiate between focal effects and spatial spillovers in regression models, but when the
diagonal is filled, then $SL_i$ becomes a consummate measure of the local environment at location
$i$.

To compute the spatial multigroup information theory index $\tilde{H}$, we first calculate local
spatially-weighted population proportions as

$$
\tilde{\pi}_{im} = \frac{SL_{im}}{\sum^M_{m=1}{SL_{im}}}
$$ {#eq:proportion}\
The density at location $i$ is 

$$
\tilde{\tau_i} = \frac{\sum^M_{m=1}{SL_{im}}}{\sum^M_{m=1}\sum^I_{i=1}{SL_{im}}}
$$ {#eq:density}\
The entropy of the local environment at each location $\tilde{E}_i$ is

$$
\tilde{E}_i = -\sum^M_{m=1}(\tilde{\pi}_{im})\log_M(\tilde{\pi}_{im})
$$ {#eq:entropy}\
where $M$ indicates the number of groups in the population. Finally, 

$$
\tilde{H} = 1-\frac{1}{TE} \sum^I \tilde{\tau_i}\tilde{E}_i
$$ {#eq:sit}\
where $\tilde{H}$ is the spatial information theory index defined by @reardon2004MeasuresSpatial. We
perform all calculations using the open-source Python package `segregation`
[@cortes2020OpensourceFramework], distributed as part of the Python Spatial Analysis Library (PySAL)
[@rey2021PySALEcosystem]

## Assessing Difference Between Distance Metrics
<!--data -->

To understand the implications of different parameterizations of space, we use data blockgroup-level
from the US Census American Community Survey (ACS) 5-year sample (2013-2017) with four
mutually-exclusive racial groups (non-Hispanic white, non-Hispanic Black, Hispanic, and Asian). Our
sample contains data for 380 metropolitan Core Based Statistical Areas (CBSAs) in the United States.
Blockgroups are the smallest geographic unit for which racial and ethnic data are available in the
ACS. To compute euclidean-based spatial segregation measures, our distances are measured between
blockgroup centroids; to compute network-based spatial segregation measures, we first attach the
blockgroup centroids to the nearest intersection in the travel network, then compute the shortest
network-based path between each pair of observations 

Our data on street networks is collected from OpenStreetMap and the shortest network path is
computed using the Python package `pandana` [@foti2012GeneralizedComputational]. To operate
efficiently on metropolitan-scale street networks, the pandana package relies on a graph
pre-processing technique known as contraction hierarchies that simplifies the computation by
removing inconsequential nodes from consideration during the routing algorithm. 



### Constructing Comparable Indices
<!-- setup the comparison -->

In each metropolitan region, we proceed by creating two different spatial weights matrices by
varying the way distance is measured between observations. In both matrices, the proximity-weighting
function $\phi$ is a simple linear decay (triangular kernel) encoding a spatial weight that
decreases with distance up to a threshold of two kilometers, outside of which observations no longer
have an effect, (that is, $r=2000$):

$$
    \phi=
\begin{cases}
    1- \left( \frac{d_{ij}}{r} \right),& \text{if } d_{ij}\leq r \\ 
    0 & \text{otherwise}
\end{cases}
$${#eq:weighting_func}\

Between the two $W$ matrices, however, we vary the input distance matrix $D$, between two concepts,
euclidean distance and network distance (where network distance is defined as the shortest path
along the pedestrian transportation network), $W_{net}$, and $W_{euc}$. In both matrices the
diagonal is set to one, indicating that there is no spatial discount for the value located at
observation $i$. Using these weights matrices $W_{net}$ and $W_{euc}$ to build local environments
for each metropolitan region in @eq:weights propagates the two constructs through
[@eq:lag; @eq:proportion; @eq:density; @eq:entropy; @eq:sit], yielding two segregation measures
$\tilde{H}_{net}$, $\tilde{H}_{euc}$ and, implicitly, a difference between the two,
$\Delta_{\tilde{H}} = \tilde{H}_{net} - \tilde{H}_{euc}$. The relative difference between segregation measures is the difference divided by the euclidean measure $\Delta_{pct} = \frac{\Delta_{\tilde{H}}}{\tilde{H}_{euc}}$


### Inferential Framework
We assess the importance of considering network distance in segregation measurement by adopting the
inferential framework outlined in @rey2021ComparativeSpatial and @cortes2020OpensourceFramework. The
approach leverages a computational approach to statistical inference using random labelling to
compare the observed difference between the two segregation measures (network versus euclidean) to a
distribution of differences generated from the same data. More specifically, the measures
$\tilde{H}_{net}$, $\tilde{H}_{euc}$ and $\Delta_{\tilde{H}}$ are computed and recorded for each metro
region. As a result of this process, two "spatialized" versions of the metropolitan demographic
composition are created, with one dataset representing euclidean distances and the other
representing network-based distances.

We then create two synthetic datasets by pooling the input units from both original datasets and
reassigning them at random. For each block-group, we randomly reassign the labels $(net,euc)$ to the
observed spatial lags from @eq:lag. Once all units have been assigned to a group, the segregation
measures are re-computed and their difference taken. This process is repeated 10,000 iterations. By
comparing the observed difference between the two segregation measures against a distribution of
differences generated via synthetic datasets, we can develop pseudo p-values based on a standard
T-test. Our test in this case measures the empirical likelihood of obtaining the observed difference
at random under the null hypothesis that the observed difference is within the standard range of
differences[^null]. The pseudo-$p$ values represent probability of obtaining results in which the
simulated difference was greater than the observed difference $\Delta_{\tilde{H}}$.


[^null]: Note this does not explicitly require the null $\Delta_{\tilde{H}}=0$. Instead the "null
value" is the mean of the simulated parameter distribution.
