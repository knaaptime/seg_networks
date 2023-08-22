---
title: Supplementary Material
bibliography: "paper-seg_networks.bib"
crossrefYaml: .pandoc/crossref_opts_supp.yaml
csl: .pandoc/csl/harvard-custom.csl
linestretch: 1.4 # for fancy_article use 1.25
geometry: margin=1in
fontsize: 10pt # for fancy_article use 11
header-includes:  | #[]  # additional latex pkgs if necessary
    \usepackage{longtable}
    \usepackage{lineno}
---

!include tables/one_pct_pandas.md

![The "Neighborhood Unit" as shown in Perry (1929)](figures/perry_neighborhood_unit.png){#fig:nup width=85%}


<div id=fig:net_vs_euc>
![Segregation based on planar and network distances by CBSA. The 45-degree line of equality is shown as dashed. ](figures/scatter.png){#fig:scatter width=45%}
![Histogram of % Differences in Segregation Measures](figures/diff_hist.png){#fig:diff_hists width=45%}

Network vs. Euclidean-based Segregation Indices
</div>

![Correlates of $\Delta_{\tilde{H}}$](figures/correlations.png){#fig:correlations width=90%}


![Network vs. Euclidean Multiscalar Segregation Profiles for Pittsburgh, PA](figures/pitt_example.png){#fig:multiscalar}


