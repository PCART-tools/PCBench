import networkx as nx
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3)])
H = nx.Graph()
H.add_edges_from([(4, 5), (5, 6)])
union_graph = nx.union(G,  H)
