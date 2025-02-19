import networkx as nx
import matplotlib.pyplot as plt

def crear_grafo():
    G = nx.Graph()

    # Agregamos los 15 nodos (0 a 14)
    for nodo in range(15):
        G.add_node(nodo)

    # Aristas sin peso (según la lista de adyacencia proporcionada)
    G.add_edge(0, 9)
    G.add_edge(0, 10)
    G.add_edge(0, 11)
    G.add_edge(0, 12)
    G.add_edge(0, 13)

    G.add_edge(1, 9)
    G.add_edge(1, 10)
    G.add_edge(1, 11)

    G.add_edge(2, 7)
    G.add_edge(2, 8)
    G.add_edge(2, 9)
    G.add_edge(2, 11)
    G.add_edge(2, 12)

    G.add_edge(3, 2)
    G.add_edge(3, 11)
    G.add_edge(3, 13)

    G.add_edge(4, 2)
    G.add_edge(4, 9)
    G.add_edge(4, 11)

    G.add_edge(5, 12)
    
    # Aquí agregamos la arista entre 5 y 6 con peso 12, como indica el profesor.
    G.add_edge(5, 6, weight=12)

    G.add_edge(6, 7)
    G.add_edge(6, 8)
    G.add_edge(6, 12)
    G.add_edge(6, 14)

    G.add_edge(7, 10)
    G.add_edge(7, 11)

    G.add_edge(8, 9)
    G.add_edge(8, 10)

    G.add_edge(9, 10)

    G.add_edge(13, 14)

    return G

def main():
    G = crear_grafo()

    # Usamos el layout automático (spring_layout)
    pos = nx.spring_layout(G, seed=42)

    # Dibujamos los nodos y aristas
    nx.draw_networkx_nodes(G, pos, node_color="skyblue", node_size=700)
    nx.draw_networkx_edges(G, pos, edge_color="gray")
    nx.draw_networkx_labels(G, pos, font_size=9, font_color="black")

    # Obtenemos y dibujamos las etiquetas de las aristas (solo se mostrarán si se asignó el atributo 'weight')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red")

    plt.title("Grafo con pesos (ejemplo)")
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    main()
