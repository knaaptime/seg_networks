# Notebooks

These notebooks comprise the analysis and should be executed in order

1. (_data) (does not yet exist yet. Pull networks and census data from quilt bucket)
2. seg_network_vs_planar
    - computes network and euclidean distance segregation measures, conducts the inference test, and writes the results to `data/network_comparison.csv`
3. network_stats
    - downloads data from OSM (in networkx format) and saves as a graphml file (1 file per metro cbsa) in `data/graphs/`
    - computes network summary stats using osmnx and saves results (1 file per metro cbsa) in `data/metrics`
4. momepy_metrics
    - reads the graphml files and computes additional network stats from `momepy`. Stores the results per metro in `data/momepy`
5. census_variables
    - get population and water/land area along with region
6. combine_datasets
    - combine osmnx, momepy, and census variables into a single dataset
7. viz_network_distance
    - create maps showing distance between isochrone and buffer
8. viz_difference_results
    - create tables and figures for the paper
9. explore_network_variables
    - look at correlation structure in network topology metrics and create figure for paper
