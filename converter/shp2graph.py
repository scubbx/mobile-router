import networkx as nx

G = nx.read_shp('vienna_austria_osm_roads.shp')
print('done reading')

# nx.write_adjlist(G,'adjlist.txt')
# adjl = nx.generate_multiline_adjlist(G,'adjlist.txt')

# nx.write_multiline_adjlist(G,'adjlist.txt')

print(nx.node_link_data(G))
