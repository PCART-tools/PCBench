import networkx as nx
G = nx.karate_club_graph()
communities = nx.community.greedy_modularity_communities(G, weight=None, resolution=1, cutoff=1, best_n=None, n_communities=None)
