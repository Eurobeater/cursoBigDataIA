import random

lista_palabras = ['portatil', 'teclado', 'raton', 'monitor', 'altavoz', 'impresora', 'disco', 'memoria', 'microfono', 'auriculares']
letras_acertadas = []
letras_falladas = []

palabra_adivinar = random.choice(lista_palabras)

print(palabra_adivinar)
print(len(palabra_adivinar))

vidas = 6

# Lista para representar el progreso del jugador con "_"
progreso_palabra = ["_"] * len(palabra_adivinar)

print("@@@@@@@@@@@@@@@@@@@ \n")
"""
def mostrar_palabra_oculta(palabra_adivinar, letra_seleccion):
    palabra_adivinar_oculta = ""

    for letra in palabra_adivinar:
        if palabra_adivinar.count(letra_seleccion) == 0:
            palabra_adivinar_oculta += "_"
        else:
            palabra_adivinar_oculta += letra

    return palabra_adivinar_oculta
"""

def mostrar_palabra_oculta():
    return " ".join(progreso_palabra)  # Convierte la lista en una cadena

def pedir_letra():
    letra_seleccion = input("Introduce una letra: ").lower()
    return letra_seleccion

"""
def checkar_letra(palabra_adivinar, letra_seleccion, vidas):
    # global vidas  # Usa la variable global, si se descomenta, quitar vidas de parámetros
    if palabra_adivinar.count(letra_seleccion) == 0:
        print("Te equivocaste")
        if letras_falladas.count(letra_seleccion) == 0:
            letras_falladas.append(letra_seleccion)

        vidas -= 1
    else:
        print("Acertaste")
        if letras_acertadas.count(letra_seleccion) == 0:
            letras_acertadas.append(letra_seleccion)

    return vidas
"""

def checkar_letra(palabra_adivinar, letra_seleccion, vidas):
    if letra_seleccion in palabra_adivinar:
        print("Acertaste")
        # Reemplaza las barras por la letra acertada en las posiciones correctas
        for i, letra in enumerate(palabra_adivinar):
            if letra == letra_seleccion:
                progreso_palabra[i] = letra_seleccion

        if letras_acertadas.count(letra_seleccion) == 0:
            letras_acertadas.append(letra_seleccion)
    else:
        print("Te equivocaste")
        if letras_falladas.count(letra_seleccion) == 0:
            letras_falladas.append(letra_seleccion)
        vidas -= 1

    return vidas

def get_letras_acertadas():
    print(f"Letras acertadas: {letras_acertadas}")

def get_letras_falladas():
    print(f"Letras falladas: {letras_falladas}")


while vidas != 0:
    print(f"Vidas: {vidas}")
    #print(mostrar_palabra_oculta(palabra_adivinar, letra_seleccion))
    print(mostrar_palabra_oculta())
    get_letras_acertadas()
    get_letras_falladas()
    letra_seleccion = pedir_letra()

    vidas = checkar_letra(palabra_adivinar, letra_seleccion, vidas)  # Actualiza vidas

    if "_" not in progreso_palabra:
        print("\n¡Felicidades! Has adivinado la palabra:")
        print(mostrar_palabra_oculta())
        break

    if vidas == 0:
        print("\n")
        print(f"Perdiste. La palabra era: {palabra_adivinar}" )
    print("\n")





