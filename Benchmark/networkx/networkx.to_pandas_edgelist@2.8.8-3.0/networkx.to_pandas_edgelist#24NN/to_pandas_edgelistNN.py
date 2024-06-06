import networkx as nx
G = nx.Graph()
G.add_edge(1, 2, weight=2)
G.add_edge(1, 3, weight=3)
G.add_edge(2, 3, weight=1)
G.add_edge(3, 4, weight=4)
edgelist = nx.to_pandas_edgelist(G,  'source',  'target', nodelist=None, dtype=None, order=None)
