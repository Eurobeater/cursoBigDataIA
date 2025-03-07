from graph import Graph, Node
from a_star import AStar

def run():
    # Create graph
    graph = Graph()
    # Add vertices
    graph.add_node(Node("A",  (2, 7)))
    graph.add_node(Node("B",  (4, 8)))
    graph.add_node(Node("C",  (3, 6)))
    graph.add_node(Node("D",  (4, 6)))
    graph.add_node(Node("E",  (6, 7)))
    graph.add_node(Node("F",  (8, 6)))
    graph.add_node(Node("G",  (9, 8)))
    graph.add_node(Node("H",  (10, 7)))
    
    # Add edges
    graph.add_edge("A",  "B",  5)
    graph.add_edge("A",  "C",  2)
    
    graph.add_edge("B",  "C",  1)
    graph.add_edge("B",  "D",  2)
    graph.add_edge("B",  "E",  4)

    graph.add_edge("C",  "D",  7)
    
    graph.add_edge("D",  "E",  1)
    
    graph.add_edge("E",  "F",  15)
    graph.add_edge("E",  "G",  12)

    graph.add_edge("F",  "G",  1)
    
    
    # Execute the algorithm
    alg = AStar(graph, "A", "E")
    path, path_length = alg.search()
    print(" -> ".join(path))
    print(f"Length of the path: {path_length}")
    
    import matplotlib.pyplot as plt
    
    plt.title("Ruta al destino")
    plt.ylim([0,10])
    plt.xlim([0,11])
    x=[]
    y=[]
    
    colores=[]
    for i in graph.nodes:
        x.append(i.x)
        y.append(i.y)
        
        plt.annotate(i.value, (i.x,i.y),xytext=(i.x+0.1,i.y+0.2))
        colores.append("green" if i.value in path else "#a0a0a0")
        vecinosx=[]
        vecinosy=[]
        for j in i.neighbors:    
            vecinosx.extend([j[0].x,i.x])
            vecinosy.extend([j[0].y,i.y])
        plt.plot(vecinosx,vecinosy,"*-k")
        
    caminox=[]
    caminoy=[]
    for indice,i in enumerate(path):
        nodo=graph.find_node(i)
        caminox.append(nodo.x)
        caminoy.append(nodo.y)
        plt.annotate(indice,(nodo.x,nodo.y),c="blue",xytext=(nodo.x+0.1,nodo.y-0.3),fontsize=8)
        
        
        
    plt.scatter(x=x,y=y,c=colores,s=100)
    plt.plot(caminox,caminoy,"*--",color="#66ff66")
    
    
    
    plt.show()
    

if __name__ == '__main__':
  run()

# S -> D -> H -> J -> K -> T
# Length of the path: 17

