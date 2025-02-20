import networkx as nx
import matplotlib.pyplot as plt
from graph import Node


nodos=[Node("A",(1,2)),
       Node("B",(2,3)),
       Node("C",(3,4)),
       Node("D",(4,2)),
       Node("E",(2,1)),
       Node("F",(3,3)),
       Node("G",(3,1))
       ]



miGrafo=nx.Graph()
for nodo in nodos:
    miGrafo.add_node(nodo.value,pos=(nodo.x,nodo.y))


miGrafo.add_edge("A","B",lenght=2)
miGrafo.add_edge("A","E",lenght=1)
miGrafo.add_edge("B","E",lenght=3)
miGrafo.add_edge("E","G",lenght=6)
miGrafo.add_edge("G","F",lenght=5)
miGrafo.add_edge("G","D",lenght=4)
miGrafo.add_edge("F","D",lenght=1)
miGrafo.add_edge("F","C",lenght=2)

labels = nx.get_edge_attributes(miGrafo,'lenght')
pos=nx.get_node_attributes(miGrafo,'pos')

print("etiquetas",labels)
print("Posiciones",pos)

nx.draw_networkx(miGrafo, pos,with_labels=True)
nx.draw_networkx_edge_labels(miGrafo, pos,edge_labels=labels)
plt.show()