class Pajaro:

    alas = True

    def __init__(self, especie, color):
        self.especie = especie
        self.color = color

    def piar(self):
        print("pio pio, mi color es {}" . format(self.color))

    def volar(self, metros):
        print(f"El pájaro ha volado {metros} metros")

piolin = Pajaro('canario', 'amarillo')

piolin.piar()
piolin.volar(50)