mi_lista = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(len(mi_lista))
print(mi_lista)

class Objeto:
    pass

mi_objeto = Objeto()
# print(len(mi_objeto)) ERROR
print(mi_objeto)

class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f"CD: {self.autor} - {self.titulo} ({self.canciones} canciones)"

    def __len__(self):
        return self.canciones

    def __del__(self):
        print("CD eliminado")

mi_cd = CD("Queen", "Greatest Hits", 12)
print(mi_cd)
print(len(mi_cd))

del mi_cd                       # Si no eliminamos el objeto, al terminar el script se eliminan todas las variables. Por eso se printea el print de la linea 32 antes que el print de la funcion del()
print("He llegado al final")