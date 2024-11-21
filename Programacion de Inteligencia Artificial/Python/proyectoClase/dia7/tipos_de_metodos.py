class Pajaro:

    alas = True

    def __init__(self, especie, color):
        self.especie = especie
        self.color = color

    def piar(self):
        print("pio pio, mi color es {}" . format(self.color))

    # Métodos de instancia pueden acceder a otros métodos
    def volar(self, metros):
        print(f"El pájaro ha volado {metros} metros")
        self.piar()     # Desde un metodo llamar al metodo piar()

    # También existen los métodos de clase,
    # que se definen con el decorador @classmethod
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} huevos')
        # Desde un método de clase puedo modificar atributos de clase
        cls.alas = False
        print(cls.alas)

    # También existen los métodos estáticos
    # No pueden acceder a atributos de instancia ni de clase
    # No pueden acceder a los métodos de instancia ni de clase
    @staticmethod
    def mirar():
        print("Estoy mirando")

piolin = Pajaro('canario', 'amarillo')

piolin.piar()
piolin.volar(50)

# Los métodos de clase no necesitan tener una instancia para ejecutarse
# No pueden acceder a atributos de instancia
Pajaro.poner_huevos(3)

# Métodos estáticos
piolin.mirar()
Pajaro.mirar()