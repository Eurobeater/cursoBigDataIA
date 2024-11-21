from dia7.metodos import piolin


class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("He nacido")

    def hablar(self):
        print("Hago ruido")

    def volar(self):
        pass
        
class Pajaro(Animal):
    # Añadir atributos a una clae hija
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

class Perro(Animal):
    pass

piolin = Pajaro(3, 'amarillo', 60)

# Metodos heredados
piolin.nacer()

# Métodos heredados y sobreescritos
piolin.hablar()

# Métooos propios
piolin.volar()

# Atributos heredados
print(piolin.edad, piolin.color)

# Atributos propios
print(piolin.altura_vuelo)