import networkx as nx
import matplotlib.pyplot as plt

def crear_grafo():
    """
    Crea un grafo ponderado basado en la tabla de adyacencia exacta.
    """
    G = nx.Graph()  # Grafo no dirigido

    # Lista de adyacencia exacta extraída de la tabla proporcionada
    edges = [
        (0, 1, 13), (0, 2, 3), (0, 3, 9), (0, 4, 4), (0, 5, 12),
        (1, 9, 9), (1, 11, 11), (1, 13, 13), (1, 10, 11), (1, 6, 12), (1, 14, 8), (1, 8, 10),
        (2, 3, 2), (2, 8, 17), (2, 0, 2), (2, 12, 4), (2, 11, 20), (2, 14, 6), (2, 13, 6),
        (3, 9, 6), (3, 12, 4), (3, 9, 8), (3, 7, 4), (3, 11, 2), (3, 4, 4), (3, 7, 10), (3, 0, 6),
        (3, 12, 19), (3, 13, 18), (3, 10, 19), (3, 12, 1),
        (4, 5, 12), (4, 9, 16), (4, 3, 8), (4, 6, 2), (4, 14, 1), (4, 11, 18),
        (5, 12, 5), (5, 8, 16), (5, 7, 20), (5, 0, 5)
    ]

    # Agregamos las aristas con sus respectivos pesos
    for u, v, peso in edges:
        G.add_edge(u, v, weight=peso)

    return G

def main():
    G = crear_grafo()

    # **Usamos un layout ordenado**
    pos = nx.kamada_kawai_layout(G)  # Organiza mejor los nodos

    # Dibujamos nodos, aristas y etiquetas de los nodos
    plt.figure(figsize=(10, 10))
    nx.draw_networkx_nodes(G, pos, node_color="skyblue", node_size=700)
    nx.draw_networkx_edges(G, pos, edge_color="gray", width=1.5)
    nx.draw_networkx_labels(G, pos, font_size=10, font_color="black", font_weight="bold")

    # **Obtenemos las etiquetas de las aristas correctamente**
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red", font_size=9)

    plt.title("Grafo Ponderado - Lista de Adyacencia", fontsize=14)
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    main()
