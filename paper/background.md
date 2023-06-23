## Incorporating Distance into Segregation Indices

In a foundational contribution, @white1983MeasurementSpatial conceives of segregation in terms of spatial
interaction, and formulates a spatial dissimilarity index using an exponential decay function to
weight the proximity between observed census units. Despite the importance of the contribution, the
application of White's technique has never become widespread, perhaps in part because of the
difficulty in operationalizing the index prior to modern GIS. Through the 1990s a surge of research
on spatial segregation indices examined different methods for incorporating space, leveraging the
growing GIS capacity of the era. An important critique of the time is given by
@wong1993SpatialIndices who shows that spatial segregation indices based on contiguity between
adjacent units provide poor definitions of the local neighborhood. This criticism is based in part
because geographic units are heterogenously-sized and also because polygon adjacency may be a poor
measurement of "nearness". Additional work has explored the sensitivitiy of segregation measures to
the modifiable areal unit problem (MAUP) [@openshaw1984EcologicalFallacies], and by extension, the
importance of spatial scale [@wong1997SpatialDependency;@wong2004ComparingTraditional]. Some authors
have also developed spatial extensions or decompositions of popular indices such as the Gini index
[@dawkins2004MeasuringSpatial;@rey2011ImpactSpatial]

In a canonical contribution to the segregation literature, @reardon2004MeasuresSpatial develop a
generalized framework for creating spatial segregation indices using a generic formulation of the
neighborhood. They also show that the spatial information theory index $\tilde{H}$ and the spatial
isolation/exposure index $\tilde{P}^\ast$ have the most desirable conceptual and mathematical
properties. @osullivan2007SurfaceBasedApproach provide an operationalization of this approach using
kernel density estimation to operationalize the notion of the neighborhood in continuous space,
overcoming many of the traditional criticisms of spatial segregation measures. In doing so, they
provided an important path forward for a body of work that has continued to expand the
notion of space.

 A variety of authors have also begun to examine the role of spatial scale. In an
 important advance in segregation methods, @reardon2008GeographicScale develop a method
 for understanding the implications of multiscalar segregation by varying the distance
 parameter used to compute the local environment in a spatial segregation index.
 Following, @reardon2009RaceSpace and @lee2008CensusTract apply the framework to a large
 set of metropolitan regions in the U.S., demonstrating a wide variety of macro versus
 micro-scaled patterns, and other work has explored the role of multiscalar change over
 time [@bailey2012HowSpatial;@fowler2016SegregationMultiscalar]. Another prominent body
 of work builds on this work, exploring the notion of "egohoods," where each household
 has its own concept of the neighborhood that extends outward and partially overlaps
 with others nearby
 [@hipp2013EgohoodsWaves;@petrovic2019FreedomTyranny;@petrovic2018MultiscaleMeasures].
 Even more recently, additional measurement techniques have been developed that help
 summarize multiscalar patterns using a single index (as opposed to an array or a ratio)
 [@bezenac2022MeasuringVisualizing;@olteanu2019SegregationMultiscalar;@osth2015MeasuringScale; @clark2015MultiscalarAnalysis].
 This research has provided clear evidence not only of the importance of considering
 spatial relationships in segregation measurement, but also the ways that
 misspecification of space (such as application of an inappropriate scale) can lead to a
 skewed concept of the phenomenon under study.

## Transportation and Social Interaction

Elsewhere, scholars have examined the role of physical barriers and built features of the urban
environment in facilitating social contact. For example @grannis2005TCommunitiesPedestrian shows
social interactions are more frequent inside "T-communities" defined by street networks
[@grannis2005TCommunitiesPedestrian], and @roberto2018SpatialProximity uses street networks to
measure segregation in a small-scale case study, and shows that segregation in Pittsburgh is higher
when measured according to network distance. These contributions emphasize a long-recognized but
understudied element of metropolitan segregation patterns, namely that transport networks, physical
barriers, and other factors such as elevation or congestion condition the expected potential for social
interaction in space. For example work in sociology has shown the importance of street network
connectivity in fostering social networks inside small urban geographic zones
[@grannis1998ImportanceTrivial]. The natural logic underlying these findings is that street networks
can help insulate urban environments and provide greater exposure to residents living inside "the
neighborhood" than those who live outside, but this distinction can be masked easily when measuring
metropolitan space using Euclidean distances.

<div id='fig:network_distance'>
![Distance Comparison in San Clemente](figures/network_distance.png){#fig:distance_sd width=40%}
![Distance Comparison in Chicago](figures/network_distance_chi.png){#fig:distance_chi width=40%}

![Distance Comparison in Cleveland](figures/network_distance_cleveland.png){#fig:distance_cleveland width=40%}
![Distance Comparison in Portland](figures/network_distance_portland.png){#fig:distance_port width=40%}

![Distance Comparison in Miami](figures/network_distance_miami.png){#fig:distance_miami width=40%}
![Distance Comparison in St Louis](figures/network_distance_stl.png){#fig:distance_stl width=40%}

Network Distance vs Euclidean Distance in Urban Environments
</div>

A depiction of the difference between network travel distance and "as the crow flies" distance is
shown in @fig:network_distance. The figure shows an origin marked with an X in the center, and two
different polygons representing a one-mile travel distance using different
methods in the cities of San Clemente and Chicago. The small
polygon depicts the total extent accessible from the origin point when traveling along the
pedestrian network, whereas the larger polygon depicts the 1-mile buffer representing unconstrained
travel. It is immediately apparent in the figure that network-constrained travel covers a much
smaller footprint than Euclidean distance in the depicted location. Furthermore, the pattern appears
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

Using evidence from a case study in Pittsburgh, @roberto2018SpatialProximity [p. 28] argues that,
"even small positive differences in the city-level results are meaningful and suggest that physical
barriers facilitate greater separation between ethnoracial groups and higher levels of segregation."
We agree with the spirit of this assessment, however, we would extend and clarify that physical
barriers themselves do not necessarily create greater separation between groups--although action by
other parts of the urban system such as inequitable land use planning or racial steering by lenders
or agents can (and does) interact with these barriers to create segregated real estate markets and
phenomena such as one group living on the "other side of the tracks"
[@roberto2018SpatialProximity]. 

Further, as @fig:network_distance shows, it is not simply the presence of physical barriers, but
also the geometric design and topological structure of the travel network that facilitates
separation between people in urban space. The curvilinear, meandering streets, and abundance of
cul-de-sacs in San Clemente stand in sharp contrast to the dense, regular grid in Chicago, even
though the network in Chicago also includes additional barriers like highways. In what follows, we
examine the magnitude of differences between network and simple Euclidean measures in detail for
every metropolitan region in the United States. Specifically, we expand upon prior work in three
different directions. First, we widen the geographic scope by considering every metropolitan region
in the United States, rather than a case study of a single city. Second, we adopt a computational
inference framework that allows us to assess whether the observed differences between the
segregation measures are large enough that they could not happen by chance. Finally, we explore the
relationship between differences in observed segregation and characteristics of the local travel
network.
