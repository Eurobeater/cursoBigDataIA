class NodoGeneral:
    def __init__(self, dato):
        self.dato = dato
        self.hijos = []

class ArbolGeneral:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato, padre=None):
        """
        Inserta un nuevo nodo en el árbol.
        Si el árbol está vacío, el nodo se convierte en la raíz.
        Si se especifica un padre, se busca ese nodo y se inserta como hijo.
        """
        nuevo_nodo = NodoGeneral(dato)

        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            nodo_padre = self.buscar(padre)
            if nodo_padre:
                nodo_padre.hijos.append(nuevo_nodo)
            else:
                print(f"Error: No se encontró el nodo padre '{padre}'.")

    def buscar(self, dato):
        """
        Busca un nodo en el árbol a partir de su dato.
        Devuelve la referencia al nodo si lo encuentra, o None en caso contrario.
        """
        return self._buscar_recursivo(self.raiz, dato)

    def _buscar_recursivo(self, nodo, dato):
        if nodo is None:
            return None
        if nodo.dato == dato:
            return nodo
        for hijo in nodo.hijos:
            encontrado = self._buscar_recursivo(hijo, dato)
            if encontrado:
                return encontrado
        return None

    def eliminar(self, dato):
        """
        Elimina un nodo del árbol.
        Si el nodo a eliminar tiene hijos, estos se reasignan al padre.
        """
        if self.raiz is None:
            return

        if self.raiz.dato == dato:
            self.raiz = None
            return

        self._eliminar_recursivo(None, self.raiz, dato)

    def _eliminar_recursivo(self, padre, nodo, dato):
        for hijo in nodo.hijos:
            if hijo.dato == dato:
                nodo.hijos.remove(hijo)
                nodo.hijos.extend(hijo.hijos)
                return True
            eliminado = self._eliminar_recursivo(nodo, hijo, dato)
            if eliminado:
                return True
        return False

    def recorrer_preorden(self):
        """
        Realiza un recorrido en preorden (raíz, luego cada uno de los hijos de izquierda a derecha)
        e imprime los datos de cada nodo.
        """
        self._recorrer_preorden(self.raiz)
        print()

    def _recorrer_preorden(self, nodo):
        if nodo is not None:
            print(nodo.dato, end=" ")
            for hijo in nodo.hijos:
                self._recorrer_preorden(hijo)

    def obtener_altura(self):
        """
        Calcula y devuelve la altura del árbol.
        """
        return self._obtener_altura_recursivo(self.raiz)

    def _obtener_altura_recursivo(self, nodo):
        if nodo is None:
            return 0
        if not nodo.hijos:
            return 1
        return max(self._obtener_altura_recursivo(hijo) for hijo in nodo.hijos) + 1

    def imprimir_arbol(self):
        """
        Imprime la estructura del árbol de forma jerárquica.
        """
        self._imprimir_recursivo(self.raiz, 0)

    def _imprimir_recursivo(self, nodo, nivel):
        if nodo is not None:
            print(" " * (nivel * 4) + f"- {nodo.dato}")
            for hijo in nodo.hijos:
                self._imprimir_recursivo(hijo, nivel + 1)

if __name__ == '__main__':
    arbol = ArbolGeneral()
    arbol.insertar("Raiz")
    arbol.insertar("Hijo1", "Raiz")
    arbol.insertar("Hijo2", "Raiz")
    arbol.insertar("Nieto1", "Hijo1")
    arbol.insertar("Nieto2", "Hijo1")
    arbol.insertar("Nieto3", "Hijo2")
    
    print("Recorrido en preorden:")
    arbol.recorrer_preorden()
    
    print("\nEstructura del árbol:")
    arbol.imprimir_arbol()
    
    print("\nAltura del árbol:", arbol.obtener_altura())
    
    print("\nEliminando el nodo 'Hijo1' y reasignando sus hijos al padre...")
    arbol.eliminar("Hijo1")
    
    print("Recorrido en preorden después de eliminar:")
    arbol.recorrer_preorden()
    
    print("\nEstructura del árbol después de eliminar:")
    arbol.imprimir_arbol()
