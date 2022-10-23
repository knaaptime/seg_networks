---
title: Segregated by Design? The Effect of Street Network Topological Structure on the Measurement of Urban Segregation
author:
- name: Elijah Knaap
  affiliation: San Diego State University
  email: eknaap@sdsu.edu
- name: Sergio Rey 
  affiliation: San Diego State University 
  email: srey@sdsu.edu 
date: October 2022 
abstract: >- 
  Racial residential segregation is a longstanding topic of focus across the disciplines of urban social science. Classically, segregation indices are calculated based on areal groupings (e.g. counties or census tracts), with more recent research exploring ways that spatial relationships can enter the equation. Spatial segregation measures embody the notion that proximity to one's neighbors is a better specification of residential segregation than simply who resides together inside the same arbitrarily-drawn polygon. Thus, they expand the notion of "who is nearby" to include those who are geographically close to each polygon rather than a binary inside/outside distinction. Yet spatial segregation measures often resort to crude measurements of proximity, such as the euclidean distance between observations, given the complexity and data requirements of calculating more theoretically-appropriate measures, such as distance along the pedestrian travel network.  In this paper, we examine the ramifications of such decisions. For each metropolitan region in the U.S., we compute both Euclidean and network-based spatial segregation indices. We use a novel inferential framework to examine the statistical significance of the difference between the two measures and following, we use features of the network topology (e.g. connectivity, circuity, throughput) to explain this difference using a series of regression models. We show that there is often a large difference between segregation indices when measured by these two strategies (which is frequently significant). Further, we explain which topology measures reduce the observed gap and discuss implications for urban planning and design paradigms
keywords: "segregation, neighborhoods, spatial analysis, network analysis, spatial weights" 
bibliography: "paper-seg_networks.bib"
crossrefYaml: .pandoc/crossref_opts.yaml
csl: .pandoc/csl/apa-custom.csl # apa without name disambiguation 
linestretch: 1.4 # for fancy_article use 1.25
geometry: margin=1in
fontsize: 10pt # for fancy_article use 11
# these do not work for fancy_article
sansitup: True
thanks: "This work is supported by NSF-SES Grant 1831615"
anonymous: False
header-includes: |
  \usepackage{mathtools} 
---


# Introduction

!include introduction.md

# Urban Infrastructure and Social Interactions

!include background.md

# The Role of Network Distance in Segregation Measurement

<!-- describe segregation measures and inference framewrok -->
!include methods_segregation.md

<!-- we show that network distance matters -->
!include results_difference.md

# Network Characteristics and Segregation Differences

<!-- treating the transport system as a network graph -->

!include methods_graphs.md

<!-- model association between network topology and segregation differences -->

!include results_graphs.md

# Discussion

!include discussion.md

# Conclusion

!include conclusion.md

# References

\setstretch{1}
