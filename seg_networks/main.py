import momepy
import networkx as nx
import numpy as np
import osmnx as ox
import pandas as pd
from geosnap import DataStore
from geosnap.io import get_acs


def generate_network_measures(msa, graph_dir="graphs", metrics_dir="metrics"):
    """Given an MSA fips code, create a dataframe of network connectivity metrics using osmnx

    Parameters
    ----------
    msa : str
        msa fips code

    Returns
    -------
    pandas.DataFrame
        dataframe containing network metrics
    """
    df = get_acs(DataStore(), years=[2019], msa_fips=msa)

    # crude area... could limit to developed area using tobler
    AREA = df.to_crs(df.estimate_utm_crs()).area.sum()

    # get a graph from the osm walk network
    msa_graph = ox.graph_from_polygon(df.unary_union, network_type="walk")

    ox.io.save_graphml(msa_graph, filepath=f"../data/{graph_dir}/{msa}_graph.graphml")

    measures = pd.DataFrame.from_dict(ox.stats.basic_stats(msa_graph, area=AREA))
    measures.to_csv(f"../data/{metrics_dir}/{msa}_measures.csv")

    return measures


def calculate_network_stats(
    msa, graph_dir="graphs", metrics_dir="metrics", area=None, save=True
):

    G = ox.io.load_graphml(f"../data/{graph_dir}/{msa}_graph.graphml")

    # unpack dicts into individiual keys:values
    stats = ox.basic_stats(G, area=area)

    for k, count in stats["streets_per_node_counts"].items():
        stats["{}way_int_count".format(k)] = count
    for k, proportion in stats["streets_per_node_proportions"].items():
        stats["{}way_int_prop".format(k)] = proportion

    # delete the no longer needed dict elements
    del stats["streets_per_node_counts"]
    del stats["streets_per_node_proportions"]

    # load as a pandas dataframe
    df = pd.DataFrame(pd.Series(stats, name="value")).round(3)
    df["avg_betweenness_centrality"] = np.mean(
        nx.betweenness_centrality(ox.get_digraph(G), weight="length").items()
    )
    df["avg_degree"] = np.mean(nx.degree(ox.get_digraph(G), weight="length").items())

    if save:
        df.to_csv(f"../data/{metrics_dir}/{msa}_measures.csv")
    return df


def generate_momepy_metrics(geoid):

    g = ox.io.load_graphml(f"../data/graphs/{geoid}_graph.graphml")

    r = dict(
        cyclomatic=momepy.cyclomatic(g, radius=None),
        meshedness=momepy.meshedness(g, radius=None),
        gamma=momepy.gamma(g, radius=None),
    )

    df = pd.DataFrame.from_dict(r, orient="index", columns=[str(geoid)]).T
    return df
