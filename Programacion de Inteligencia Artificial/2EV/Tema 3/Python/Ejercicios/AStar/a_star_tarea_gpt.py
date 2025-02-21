from graph import Graph, Node
from a_star import AStar

def run():
    # Create graph
    graph = Graph()
    # Add vertices
    # ================
    # 1) Añadimos 15 nodos (0..14) con coordenadas (x,y)
    #    (Estas coordenadas son ficticias; ajústalas si quieres
    #     que la distancia Manhattan sea más fiel a tu imagen)
    # ================
    graph.add_node(Node("0",  (2, 5)))
    graph.add_node(Node("1",  (10, 1)))
    graph.add_node(Node("2",  (4, 4)))
    graph.add_node(Node("3",  (1, 3)))
    graph.add_node(Node("4",  (6, 3)))
    graph.add_node(Node("5",  (3, 8)))
    graph.add_node(Node("6",  (4, 9)))
    graph.add_node(Node("7",  (2, 2)))
    graph.add_node(Node("8",  (6, 2)))
    graph.add_node(Node("9",  (7, 3)))
    graph.add_node(Node("10", (9, 1)))
    graph.add_node(Node("11", (3, 4)))
    graph.add_node(Node("12", (5, 6)))
    graph.add_node(Node("13", (1, 6)))
    graph.add_node(Node("14", (8, 9)))
    
    # Add edges
    # ================
    # 2) Agregamos las aristas (conexiones) con sus pesos.
    #    Aquí pongo un ejemplo basado en tu tabla final.
    #    Ajusta o quita/pon conexiones según tu grafo real.
    # ================
    # Formato: graph.add_edge("nodo1", "nodo2", peso)

    graph.add_edge("0",  "13",  13)
    graph.add_edge("0",  "3",  2)
    graph.add_edge("0",  "9",  6)
    graph.add_edge("0",  "4",  18)
    graph.add_edge("0",  "12",  5)
    
    graph.add_edge("1",  "9",  9)
    
    graph.add_edge("2",  "11",  11)
    graph.add_edge("2",  "8",  17)
    graph.add_edge("2",  "12",  4)
    
    graph.add_edge("3",  "13",  11)
    #graph.add_edge("3",  "0",  2)
    graph.add_edge("3",  "9",  8)
    
    graph.add_edge("4",  "10",  11)
    #graph.add_edge("4",  "0",  18)
    graph.add_edge("4",  "7",  4)
    
    graph.add_edge("5",  "6",  12)
    
    graph.add_edge("6",  "14",  8)
    graph.add_edge("6",  "12",  4)
    graph.add_edge("6",  "11",  2)
    #graph.add_edge("6",  "5",  12)
    
    graph.add_edge("7",  "8",  10)
    graph.add_edge("7",  "11",  20)
    #graph.add_edge("7",  "4",  4)
    
    graph.add_edge("8",  "11",  9)
    #graph.add_edge("8",  "2",  17)
    #graph.add_edge("8",  "7",  10)
    graph.add_edge("8",  "9",  16)
    
    graph.add_edge("9",  "10",  9)
    #graph.add_edge("9",  "1",  9)
    #graph.add_edge("9",  "0",  6)
    #graph.add_edge("9",  "3",  8)
    #graph.add_edge("9",  "8",  16)
    
    #graph.add_edge("10",  "4",  11)
    #graph.add_edge("10",  "9",  9)
    graph.add_edge("10",  "12",  19)
    
    #graph.add_edge("11",  "2",  11)
    #graph.add_edge("11",  "8",  9)
    graph.add_edge("11",  "13",  18)
    #graph.add_edge("11",  "6",  2)
    #graph.add_edge("11",  "7",  20)
    
    #graph.add_edge("12",  "6",  4)
    #graph.add_edge("12",  "2",  4)
    #graph.add_edge("12",  "10",  19)
    graph.add_edge("12",  "14",  1)
    #graph.add_edge("12",  "0",  5)
    
    #graph.add_edge("13",  "0",  13)
    graph.add_edge("13",  "14",  6)
    #graph.add_edge("13",  "3",  11)
    #graph.add_edge("13",  "11",  18)
    
    #graph.add_edge("14",  "6",  8)
    #graph.add_edge("14",  "13",  6)
    #graph.add_edge("14",  "12",  1)
    
    # Execute the algorithm
    # ================
    # 3) Ejecutamos A* para ir del nodo "5" al nodo "1"
    # ================
    alg = AStar(graph, "5", "1")
    path, path_length = alg.search()
    print(" -> ".join(path))
    print(f"Length of the path: {path_length}")
    
    import matplotlib.pyplot as plt
    
    # ================
    # 4) Visualizamos
    #    Dibujamos el grafo y marcamos la ruta en verde
    # ================
    plt.title("Ruta al destino")
    #plt.ylim([0,5])
    #plt.xlim([0,5])
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

