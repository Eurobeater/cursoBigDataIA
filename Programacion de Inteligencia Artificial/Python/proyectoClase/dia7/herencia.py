class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("He nacido")

class Pajaro(Animal):       # Hereda de Animal
    pass

class Perro(Animal):
    pass

print(Pajaro.__bases__)             # Mostrar la clase de la que viene Pajaro
print(Animal.__subclasses__())      # Mostrar las subclases de la clase Animal

piolin = Pajaro(2, "amarillo")
piolin.nacer()

print(piolin.edad, piolin.color)