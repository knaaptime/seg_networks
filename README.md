# Segregated by Design? The Effect of Street Network Topological Structure on the Measurement of Urban Segregation

this project examines the relationship between pedestrian network characteristics and the measurement of metropolitan segregation.
It examines three questions:

1. How large is the difference between euclidean-based and network-based measures of spatial segregation?
   1. how often
   2. where?
2. Are the differences between euclidean and network measures significantly different from random realizations of the same data?
   - how often
   - where 
3. what characteristics of the pedestrian network explain the observed difference in measurement?

## To Do

- [ ] attach census data to street network, then drop nodes with NA values and recalculate euclidean segregation on this surface
  - this ensures its 1:1 because otherwise we shift the observations slightly to align with network-based measures
- [ ] make sure the new decay methods in segregation match the [logic from pandana](https://github.com/UDST/pandana/blob/3e3d35ca2d57428714b89ed8fc7020bc55067e1d/src/accessibility.cpp#L391)
- [ ] add graph measures [from momepy](http://docs.momepy.org/en/stable/api.html#graph)


## Datasets

It takes a long time (around a day, IIRC) to loop over all the metros, download all the network data
from OSM, and store it as a graphML file. Instead, you can
[download the directory](https://www.dropbox.com/sh/r68xdioea0icrtp/AABHVFfJcC81v3AdPctsl1dGa?dl=0)
I already computed with the notebook `notebooks/network_stats.ipynb`. That should live in
`/data/graphs`. We can commit a few graphs to the repository for demonstration (maybe SD?)

You can read the GraphML files with networkx, momepy, or osmnx. You can also create a
pandana.Network from the graph you instantiate from osmnx, so these files are all we need to compute
graph metrics or shortest-paths.

## Set up

**The conda environment contains _all_ necessary dependencies**

1. clone this repository
2. run `make environment` to build the conda environment with necessary dependencies
   - run `conda activate seg_networks` each time you work on the project
   - run `make environment-update` to rebuild the conda environment if you add new dependencies or they change upstream
