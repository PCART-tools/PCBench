import networkx as nx
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3)])
values = {1: 'A', 2: 'B', 3: 'C'}
nx.set_node_attributes(G,  'color',  values)
