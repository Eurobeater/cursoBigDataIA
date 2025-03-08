from graph import Graph, Node
import matplotlib.pyplot as plt
from math import inf

def dibujar_grafo(grafo):
    plt.figure(figsize=(8, 6))
    plt.title("Grafo")
    plt.xlabel("X")
    plt.ylabel("Y")
    
    aristas_dibujadas = []
    
    for nodo in grafo.nodes:
        plt.scatter(nodo.x, nodo.y, c='blue', s=100)
        plt.text(nodo.x + 0.1, nodo.y + 0.1, nodo.value, fontsize=10)
        
        for vecino, costo in nodo.neighbors:
            # Identificamos la arista de forma única ordenando los nombres de los nodos.
            arista = sorted([nodo.value, vecino.value])
            if arista not in aristas_dibujadas:
                plt.plot([nodo.x, vecino.x], [nodo.y, vecino.y], 'k-')
                xm = (nodo.x + vecino.x) / 2
                ym = (nodo.y + vecino.y) / 2
                plt.text(xm, ym, str(costo), color='red', fontsize=9)
                aristas_dibujadas.append(arista)
    
    plt.grid(True)

def reset_graph(grafo):
    """
    Reestablece los atributos de cada nodo del grafo:
    - Establece el padre (parent) a None.
    - Pone el valor heurístico (heuristic_value) a -1.
    - Establece la distancia desde el inicio (distance_from_start) a infinito.
    """
    for nodo in grafo.nodes:
        nodo.parent = None
        nodo.heuristic_value = -1
        nodo.distance_from_start = inf

def main():
    # Crear el grafo y añadir nodos
    grafo = Graph()
    
    grafo.add_node(Node("A", (2, 7)))
    grafo.add_node(Node("B", (4, 8)))
    grafo.add_node(Node("C", (3, 6)))
    grafo.add_node(Node("D", (4, 6)))
    grafo.add_node(Node("E", (6, 7)))
    grafo.add_node(Node("F", (8, 6)))
    grafo.add_node(Node("G", (9, 8)))
    grafo.add_node(Node("H", (10, 7)))
    
    # Añadir aristas con sus costes
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
    
    # Dibujar el grafo
    dibujar_grafo(grafo)
    plt.show()
    
    # Reiniciar el grafo (borrar rastros de búsquedas anteriores)
    reset_graph(grafo)
    
    # Mostrar la información solicitada
    print("\nVerificar reseteo")
    for nodo in grafo.nodes:
        print(nodo.value, nodo.parent, nodo.heuristic_value, nodo.distance_from_start)
    
    print("¿Están conectados G y H?", grafo.are_connected("G", "H"))
    print("¿Están conectados D y E?", grafo.are_connected("D", "E"))
    print("Número de nodos:", len(grafo.nodes))
    print("Lista de nodos:", [nodo.value for nodo in grafo.nodes])

if __name__ == "__main__":
    main()
