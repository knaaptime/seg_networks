## Network Distance is an Important Consideration

Although the Pearson correlation between planar and network based segregation measures
is $\rho=0.987$, our results provide clear evidence that the choice of appropriate
distance metric plays an important role in the computation of a spatial segregation
index. We highlight this result using the fact that applied segregation research often
uses ordinal rankings to describe and compare the magnitude of segregation across a set
of places. While still high, the *rank correlation* between the two measures is
considerably lower at $\tau=0.90$. Substantively, this means that an analysis of
segregated metropolitan regions will result in different conclusions regarding the "most
segregated" places, depending on which distance measure is employed. A visual comparison
of the top 15 most segregated metros is provided in @fig:ranks, demonstrating how
different places exchange ranks, and @fig:scatter in the supplementary material portrays the
relationship between segregation measured using the two different distance metrics for
the sample CBSAs.

![Planar vs. Network Segregation Rankings](figures/ranks.png){#fig:ranks
width=90%}

When measured in absolute terms, essentially every metropolitan region exhibits higher
segregation when measured according to network distance than by pure Euclidean
distance[^CRS], with only four exceptions (none of the four cases are significantly
different from a random pooling of the same data). Among the 380 CBSAs in our dataset,
25.3% have a difference between Euclidean and network-based segregation measures that is
significant at the $\alpha=0.05$ level, and 14.2% of the CBSAs are significant at the
$\alpha=0.01$ level. Descriptive statistics of the differences between segregation
measures in each metro are shown in @tbl:diff_descriptives, and a list of the 54 CBSAs
significant at the one percent level are listed in @tbl:one_pct_diffs. Among these 54
CBAS, eight metros are located in California--twice the number of the next-most
prevalent state (Texas).

!include tables/difference_descriptives_pandas.md

The distributions of both $\Delta_{\tilde{H}}$ and $\Delta_{pct}$ are normally-shaped
with respective means of 0.029 and 0.198 respectively. While the absolute difference
between the two segregation measures in each CBSA can appear small, the relative
difference is often reasonably large, with the network-based segregation measure
approximately 20% higher than the Euclidean-based measure on average. The largest
relative difference gets as high as 69% (Carson City, NV), and the smallest differences
are zero (Hattiesburg, MS, Longview, TX, Rocky Mount, NC, and California-Lexington Park,
MD). 

<!-- Do a quick Moran using KNN?  Maybe using join counts for significant/not?-->

[^CRS]: For each CBSA in our sample, our Euclidean distances are based on UTM coordinate systems,
with each region's data projected into its appropriate UTM zone.
