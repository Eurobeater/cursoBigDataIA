import networkx as nx
g = nx.Graph()

# Add vertices
g.add_node('S', pos=(1,1))
g.add_node('B', pos=(1,2))
g.add_node('C', pos=(1,4))
g.add_node('D', pos=(2,1))
g.add_node('E', pos=(2,2))
g.add_node('F', pos=(2,3))
g.add_node('G', pos=(2,4))
g.add_node('H', pos=(3,1))
g.add_node('I', pos=(3,4))
g.add_node('J', pos=(4,1))
g.add_node('K', pos=(4,2))
g.add_node('T', pos=(4,3))
g.add_node('L', pos=(4,4))


g.add_edge('S', 'B', lenght=4)    
g.add_edge('S', 'D', lenght=5)
g.add_edge('B', 'E', lenght=1)
g.add_edge('C', 'G', lenght=1)
g.add_edge('D', 'E', lenght=2)
g.add_edge('D', 'H', lenght=3)
g.add_edge('E', 'F', lenght=6)
g.add_edge('F', 'G', lenght=4)
g.add_edge('G', 'I', lenght=3)
g.add_edge('H', 'J', lenght=1)
g.add_edge('I', 'L', lenght=4)
g.add_edge('J', 'K', lenght=6)
g.add_edge('K', 'T', lenght=2)
g.add_edge('T', 'L', lenght=3)

labels = nx.get_edge_attributes(g,'lenght')
pos=nx.get_node_attributes(g,'pos')

print("etiquetas",labels)
print("Posiciones",pos)
nx.draw_networkx(g, pos,with_labels=True)
nx.draw_networkx_edge_labels(g, pos,edge_labels=labels)

