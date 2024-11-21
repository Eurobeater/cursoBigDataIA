class Padre:
    def hablar(self):
        print("Hola, yo soy tu padre")

class Madre:
    def hablar(self):
        print("Hola, yo soy tu madre")

    def reir(self):
        print("ja ja ja")

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

print(Nieto.__bases__)      # Nieto hereda de Hijo
pepe = Nieto()
pepe.hablar()       # Imprime 'Hola, yo soy tu padre'. Porque primero hereda la clase Padre
pepe.reir()

print(Nieto.__mro__)