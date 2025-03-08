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
            arista = sorted([nodo.value, vecino.value])
            if arista not in aristas_dibujadas:
                plt.plot([nodo.x, vecino.x], [nodo.y, vecino.y], 'k-')
                xm = (nodo.x + vecino.x) / 2
                ym = (nodo.y + vecino.y) / 2
                plt.text(xm, ym, str(costo), color='red', fontsize=9)
                aristas_dibujadas.append(arista)
    
    plt.grid(True)

def reset_graph(grafo):
    for nodo in grafo.nodes:
        nodo.parent = None
        nodo.heuristic_value = -1
        nodo.distance_from_start = inf

def main():
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
    
    dibujar_grafo(grafo)
    plt.show()
    
    reset_graph(grafo)
    
    # Verificar restauración de los valores
    print("\nVerificar reseteo")
    for nodo in grafo.nodes:
        print(nodo.value, nodo.parent, nodo.heuristic_value, nodo.distance_from_start)
    
    nodo_B = grafo.find_node("B")
    vecinos_B = [vecino[0].value for vecino in nodo_B.neighbors]
    print("Vecinos del nodo B:", vecinos_B)
    
    print("¿Están conectados G y H?", grafo.are_connected("G", "H"))
    print("¿Están conectados D y E?", grafo.are_connected("D", "E"))
    print("Número de nodos:", len(grafo.nodes))
    print("Lista de nodos:", [nodo.value for nodo in grafo.nodes])

main()
