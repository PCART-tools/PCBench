import networkx as nx
G = nx.Graph()
G.add_weighted_edges_from([(1, 2, 3.0), (2, 3, 2.0), (3, 4, 1.0), (4, 1, 4.0)])
matching = nx.min_weight_matching(G=G, maxcardinality=None, weight='weight')
