from a_star import AStar
from graph import Graph, Node, inf

def reset_graph(grafo):
    for nodo in grafo.nodes:
        nodo.parent = None
        nodo.heuristic_value = -1
        nodo.distance_from_start = inf

def ruta(origen, destino, grafo):
    algoritmo = AStar(grafo, origen, destino)
    resultado = algoritmo.search()
    
    if resultado:
        camino, coste = resultado
        print("Ruta:", " -> ".join(camino))
        print("Coste total:", coste)
    else:
        print(f"No se encontró ruta desde {origen} hasta {destino}.")

grafo = Graph()

grafo.add_node(Node("A", (2, 7)))
grafo.add_node(Node("B", (4, 8)))
grafo.add_node(Node("C", (3, 6)))
grafo.add_node(Node("D", (4, 6)))
grafo.add_node(Node("E", (6, 7)))
grafo.add_node(Node("F", (8, 6)))
grafo.add_node(Node("G", (9, 8)))
grafo.add_node(Node("H", (10, 7)))
    
grafo.add_edge("A", "B", 5)
grafo.add_edge("A", "C", 2)
grafo.add_edge("B", "C", 1)
grafo.add_edge("B", "D", 2)
grafo.add_edge("B", "E", 4)
grafo.add_edge("C", "D", 7)
grafo.add_edge("D", "E", 1)
grafo.add_edge("E", "F", 15)
grafo.add_edge("E", "G", 12)
grafo.add_edge("F", "G", 1)

print("Camino más corto entre A y B")
ruta("A", "B", grafo)
reset_graph(grafo)

print("\nCamino más corto entre A y G")
ruta("A", "G", grafo)
reset_graph(grafo)

print("\nCamino más corto entre A y H")
ruta("A", "H", grafo)
reset_graph(grafo)

print("\nCamino más corto entre G y C")
ruta("G", "C", grafo)
