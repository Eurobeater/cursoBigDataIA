class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._insertar_recursivo(self.raiz, dato)

    def _insertar_recursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(dato)
            else:
                self._insertar_recursivo(nodo.izquierdo, dato)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(dato)
            else:
                self._insertar_recursivo(nodo.derecho, dato)

    def recorrer_en_orden(self, nodo):
        if nodo is not None:
            self.recorrer_en_orden(nodo.izquierdo)
            print(nodo.dato, end=" ")
            self.recorrer_en_orden(nodo.derecho)

    def buscar(self, dato):
        return self._buscar_recursivo(self.raiz, dato)

    def _buscar_recursivo(self, nodo, dato):
        if nodo is None:
            return False
        if nodo.dato == dato:
            return True
        if dato < nodo.dato:
            return self._buscar_recursivo(nodo.izquierdo, dato)
        else:
            return self._buscar_recursivo(nodo.derecho, dato)

    def eliminar(self, dato):
        self.raiz = self._eliminar_recursivo(self.raiz, dato)

    def _eliminar_recursivo(self, nodo, dato):
        if nodo is None:
            return None
        if dato < nodo.dato:
            nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, dato)
        elif dato > nodo.dato:
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, dato)
        else:
            if nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo
            sucesor = self._encontrar_minimo(nodo.derecho)
            nodo.dato = sucesor.dato
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, sucesor.dato)
        return nodo

    def _encontrar_minimo(self, nodo):
        while nodo.izquierdo is not None:
            nodo = nodo.izquierdo
        return nodo

    def obtener_altura(self):
        return self._obtener_altura_recursivo(self.raiz)

    def _obtener_altura_recursivo(self, nodo):
        if nodo is None:
            return -1
        izquierda = self._obtener_altura_recursivo(nodo.izquierdo)
        derecha = self._obtener_altura_recursivo(nodo.derecho)
        return max(izquierda, derecha) + 1

arbol = ArbolBinario()

valores = ["H", "F", "B", "A", "D", "G", "J", "I", "K"]
for v in valores:
    arbol.insertar(v)

print("Recorrido en orden (ascendente):")
arbol.recorrer_en_orden(arbol.raiz)
print("\n")

buscar_valores = ["A", "J", "Z"]
for v in buscar_valores:
    encontrado = arbol.buscar(v)
    print(f"¿El valor '{v}' está en el árbol?: {'Sí' if encontrado else 'No'}")

altura_antes = arbol.obtener_altura()
print(f"\nAltura del árbol antes de eliminaciones: {altura_antes}")

arbol.eliminar("F")
arbol.eliminar("J")

print("\nRecorrido en orden después de eliminar F y J:")
arbol.recorrer_en_orden(arbol.raiz)
print("\n")

altura_despues = arbol.obtener_altura()
print(f"Altura del árbol después de eliminaciones: {altura_despues}")
