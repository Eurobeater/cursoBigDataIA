class Pajaro:
    # This is a contructor
    def __init__(self, especie, color):   # self hace que se refiera al objeto en sí mismo
        self.especie = especie
        self.color = color

mi_pajaro = Pajaro("Tucán", "Azul")     # Crear un objeto de la clase Pajaro

print(mi_pajaro.especie)
print(mi_pajaro.color)

print(f"Mi pájaro es un {mi_pajaro.especie} de color {mi_pajaro.color}")

class Pajaro:

    alas = True

    # This is a contructor
    def __init__(self, especie, color):   # self hace que se refiera al objeto en sí mismo
        self.especie = especie
        self.color = color

mi_pajaro2 = Pajaro("Periquito", "Negro")
print(f"Mi pájaro es un {mi_pajaro.especie} de color {mi_pajaro.color}")
print(Pajaro.alas)
print(mi_pajaro2.alas)
# print(mi_pajaro.alas) ERROR