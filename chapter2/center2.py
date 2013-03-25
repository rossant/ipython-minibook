import networkx as nx
g = nx.read_edgelist('data/facebook/0.edges')
sg = nx.connected_component_subgraphs(g)[0]
# we compute the eccentricity once, for all nodes
ecc = nx.eccentricity(sg)
# we compute the radius once
r = nx.radius(sg)
center = [node for node in sg.nodes() if ecc[node] == r]
print(center)
