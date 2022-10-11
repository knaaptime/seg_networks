<!-- Hook -->

An exceedingly common abstraction in applied spatial analysis is the use of euclidean distance as a
proxy measure for geographic proximity (which is, itself, often a proxy for the frequency of social
interaction). It's the geographic equivalent of
[the spherical cow](https://en.wikipedia.org/wiki/Spherical_cow), save that scientists of many
different disciplines often fail to realize how simplified it is. While, in general, simple
proximity is a reasonable heuristic for understanding Tobler's Law, the behavioral realities of
movement and social interaction in complex urban environments often require a more thoughtful model.


<!-- Question -->

this project examines the relationship between pedestrian network characteristics and the measurement of metropolitan segregation.
It examines three questions:

1. How large is the difference between euclidean-based and network-based measures of spatial segregation?
   1. how often
   2. where?
2. Are the differences between euclidean and network measures significantly different from random realizations of the same data?
   - how often
   - where 
3. what characteristics of the pedestrian network explain the observed difference in measurement?

<!-- Antecedents -->

*really* quick overview of normative concepts of community and urban design... Daniel Burnham, Le Corbusier, Ebenezeer Howard, James Rouse, and... Emily Talen


how do we represent space in social science research?

classics:
- sociology uses groups. Neighborhoods or cities are discrete containers that condition social behaviors (Park, Burgess, McKenzie)
- econ and regional science use distance from the city center
    - ultimately about transport of goods (von thunen was based on an *agricultural economy* and moving crops from the ag hinterlands into the marketplace where people actually lived). 
    - Transport connectivity is implicit, but models are high-level in the 1950s, and the abstraction works conceptually. Neither the theory or computational power exist yet to examine the role of better measurements of $W_{ij}$
recents:
- GIS, geography, and spatial econometrics concepts of spatial weights
- multiscale and/or bespoke neighborhoods in geography and sociology (Hipp, van Ham, )
- street networks in empirical work
    - grannis shows social interactions are more frequent inside T-communities defined by street networks
    - Roberto uses street networks to measure segregation in a small-scale case study.

<!-- Value-Added -->

Now we have both the tools and the logic to test these assumptions and understand the role of
abstractions such as euclidean distance-based measures in our assessment of critical social
processes such as residential segregation. Fast graph algorithms allow us to construct more
realistic concepts of spatial weights matrices, and computational statistics allow us to construct
and test realistic null hypotheses about the allocation of urban population groups. Here, we examine
the role of street network topology in the appropriate measurement of urban segregation. Our goals
are twofold. First, we aim to understand the implications of simple Euclidean distance- based
abstractions when conducting formal spatial analyses; that is, do we find substantive differences in
results when more realistic concepts of spatial relationships (e.g. network connectivity) are
considered? Second, we aim to explore the elements of urban design (particularly the street network
configuration) in widening the gap between analytical abstraction and empirical reality. More
simply, we aim to understand whether certain elements of the street network are associated with a
greater difference in measured segregation. With this knowledge, urban designers and planners can
begin with more inclusive communities from the beginning.

<!-- Road-map -->



