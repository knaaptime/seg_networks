# Segregated by Design? Street Network Topological Structure & the Measurement of Urban Segregation

code for accompanying paper. Forthcoming in EPB. 

**Note**, I often use
papers to draft the first version of methods that are eventually implemented in other packages like
`segregation`, `geosnap`, or elsewhere in the PySAL stack. So while the code in here *should* run, it is probably more efficient
or possibly outdated in the newest versions of those packages. Follow along at your own risk :)

## Datasets

It takes a long time (around a day, IIRC) to loop over all the metros, download all the network data
from OSM, and store each as a graphML file. You've been warned

## Set up

**The conda environment contains _all_ necessary dependencies**

1. clone this repository
2. run `make environment` to build the conda environment with necessary dependencies
   - run `conda activate seg_networks` each time you work on the project
   - run `make environment-update` to rebuild the conda environment if you add new dependencies or they change upstream
