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

    def recorrer_en_orden(self, nodo):
        if nodo is not None:
            self.recorrer_en_orden(nodo.izquierdo)
            print(nodo.dato, end=" ")
            self.recorrer_en_orden(nodo.derecho)

    def obtener_altura(self):
        return self._obtener_altura_recursivo(self.raiz)

    def _obtener_altura_recursivo(self, nodo):
        if nodo is None:
            return -1
        izquierda = self._obtener_altura_recursivo(nodo.izquierdo)
        derecha = self._obtener_altura_recursivo(nodo.derecho)
        return max(izquierda, derecha) + 1

# Ejemplo de uso
arbol = ArbolBinario()
arbol.insertar(50)
arbol.insertar(30)
arbol.insertar(70)
arbol.insertar(20)
arbol.insertar(40)
arbol.insertar(60)
arbol.insertar(80)

print("Recorrido en orden:")
arbol.recorrer_en_orden(arbol.raiz)  # 20 30 40 50 60 70 80

print("\nAltura del árbol:", arbol.obtener_altura())

print("\nBuscar 40:", arbol.buscar(40))  # True
print("Buscar 100:", arbol.buscar(100))  # False

print("\nEliminar 70")
arbol.eliminar(70)

print("Recorrido en orden después de eliminar 70:")
arbol.recorrer_en_orden(arbol.raiz)  # 20 30 40 50 60 80
