
Classically, space is treated as a discrete concept, by membership in a group (i.e. a school,
classroom, neighborhood, or city), where any of these groupings is defined exogenously.

## The Role of Space in Segregation Measurement

### Making Space Explicit

@reardon2004MeasuresSpatial
@reardon2009RaceSpace
@wong1997SpatialDependency
@bailey2012HowSpatial
@rey2011ImpactSpatial
@osullivan2007SurfaceBasedApproach
@wong2004ComparingTraditional
@dawkins2004MeasuringSpatial

### Interrogating Spatial Scale

@lee2008CensusTract
@reardon2008GeographicScale
@bezenac2022MeasuringVisualizing
@olteanu2019SegregationMultiscalar
@osth2015MeasuringScale
@clark2015MultiscalarAnalysis


## Homogenous Communities and Urban Design

A long-recognized but understudied element of metropolitan segregation patterns is the role of
transport networks, physical barriers, and other factors such as elevation or congestion that change
travel behavior, and thus, the expected potential for social interaction in space. For example work
in sociology has shown the importance of street network connectivity in fostering connected social
networks inside small urban geographic zones [@grannis1998ImportanceTrivial]. 

@grannis2005TCommunitiesPedestrian

<div id='fig:network_distance'>
![Network Distance vs Euclidean Distance](figures/network_distance.png){#fig:distance_sd width=49%}
![Network Distance vs Euclidean Distance](figures/network_distance_chi.png){#fig:distance_chi width=49%}

Network Distance vs Euclidean Distance in Urban Environments
</div>

A depiction of the difference between network travel distance and "as the crow flies" distance is
shown in @fig:network_distance. The figure shows an origin marked with an X in the center, and two
different polygons representing a one-mile travel distance using different methods. The small
polygon depicts the total extent accessible from the origin point when traveling along the
pedestrian network, whereas the larger polygon depicts the 1-mile buffer representing unconstrained
travel. It is immediately apparent in the figure that network-constrained travel covers a much
smaller footprint than euclidean distance in the depicted location. Furthermore, the pattern appears
to be influenced strongly by the street network and urban design features that characterize the
largely suburban region of San Clemente.

Instead of a regular grid that facilitates travel in all directions (like the densely urbanized
section of Chicago in @fig:distance_chi), the street network in @fig:distance_sd includes several
insular patterns, cul-de-sacs, and 3-way intersections that help channel traffic in certain
directions rather than others. Furthermore, the fact that some subdivisions have only a single
entrance makes clear how much further a person would need to travel to reach the homes in certain
regions (versus how much easier they appear to be reached via the circular buffer). By contrast, the
regular gridded pattern in Chicago in @fig:distance_chi allows travel to flow in all directions.
Because the origin starts on a street oriented East-West, the polygon covers essentially the entire
circular buffer in that direction. The North-South direction is limited, however for two reasons,
first, the traveler needs to reach a cross street before changing direction, and second the Kennedy
expressway provides a man-made physical barrier that impedes travel in the southwestern direction,
creating a hard edge in the inner polygon except along a single passageway. A similar phenomenon
impedes traffic in the northward direction, as the network does not extend into Saint Luke Cemetery.

Recent work by @roberto2018SpatialProximity shows the importance of considering network distances
when measuring segregation using both simulated data and an empirical example in Pittsburgh, PA.
That study shows that segregation is consistently higher at all spatial scales when the measure
accounts for local network connectivity. As @roberto2018SpatialProximity [p. 28] notes, "even small
positive differences in the city-level results are meaningful and suggest that physical barriers
facilitate greater separation between ethnoracial groups and higher levels of segregation." We agree
with the spirit of this assessment, however, we would extend and clarify that physical barriers
themselves do not necessarily create greater separation between groups--although action by other
parts of the urban system such as racial steering by lenders or agents can (and does) interact with
these barriers to create segregated real estate markets and phenomena such as one group living on
the "other side of the tracks" [@roberto2018SpatialProximity].

Further, as @fig:network_distance shows, it is not simply the presence of physical barriers, but
also the geometric design and topological structure of the travel network that facilitates
separation between people in urban space. The curvilinear, meandering streets and abundance of
cul-de-sacs in San Clemente stand in sharp contrast to the dense, regular grid in Chicago, even
though the network in Chicago also includes additional barriers like highways. In what follows, we
examine the magnitude of differences between network and simple euclidean measures in detail for
every metropolitan region in the United States. Specifically, we expand upon prior work in three
different directions. First, we expand the geographic scope by considering every metropolitan region
in the United States, rather than a case study of a single city. Second, we adopt a computational
inference framework that allows us to assess whether the observed differences between the
segregation measures are large enough that they could not happen by chance. Finally, we explore the
relationship between differences in observed segregation and characteristics of the local travel
network.
