import networkx as nx
import matplotlib.pyplot as plt

def crear_grafo():
    G = nx.Graph()  # Grafo NO dirigido

    # Lista de adyacencia basada en la tabla proporcionada (con pesos corregidos)
    edges = [
        (0, 1, 13), (0, 2, 2), (0, 3, 6), (0, 4, 18), (0, 5, 12),
        (1, 2, 11), (1, 3, 11), (1, 4, 11), (1, 5, 12), (1, 6, 8), (1, 7, 10), (1, 8, 9), (1, 9, 9), (1, 10, 11),
        (1, 11, 11), (1, 12, 4), (1, 13, 13), (1, 14, 8),
        (2, 3, 4), (2, 4, 18), (2, 6, 4), (2, 7, 20), (2, 8, 17), (2, 9, 9), (2, 10, 9), (2, 11, 9), (2, 12, 4),
        (2, 13, 6), (2, 14, 6),
        (3, 4, 4), (3, 6, 2), (3, 7, 4), (3, 8, 10), (3, 9, 6), (3, 10, 19), (3, 11, 18), (3, 12, 19),
        (3, 13, 11), (3, 14, 1),
        (4, 6, 12), (4, 8, 16), (4, 9, 8), (4, 11, 2), (4, 12, 1), (4, 13, 18),
        (5, 9, 16), (5, 11, 20), (5, 12, 5),
        (6, 14, 8)
    ]

    # Agregar las conexiones al grafo
    for u, v, peso in edges:
        G.add_edge(u, v, weight=peso)

    return G

def main():
    G = crear_grafo()

    # Layout ordenado para mejorar la legibilidad del grafo
    pos = nx.spring_layout(G, seed=42, k=0.35)  # Ajustar k para distribuir mejor los nodos

    # Dibujar nodos, aristas y etiquetas
    plt.figure(figsize=(14, 14))
    nx.draw_networkx_nodes(G, pos, node_color="skyblue", node_size=800)
    nx.draw_networkx_edges(G, pos, edge_color="gray", width=1.5)
    nx.draw_networkx_labels(G, pos, font_size=12, font_color="black", font_weight="bold")

    # Etiquetas de los pesos corregidos
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red", font_size=9)

    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    main()
