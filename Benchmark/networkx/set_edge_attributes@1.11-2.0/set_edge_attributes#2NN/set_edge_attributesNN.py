import networkx as nx
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3)])
values = {(1, 2): 'red', (2, 3): 'blue'}
nx.set_edge_attributes(G,  'color', values=values)
