prueba_numeros = [5, 10, 15]

for i in range(len(prueba_numeros)):
    print(f"Índice: {i}, Número: {prueba_numeros[i]}")



def devolver_distintos(numero_1, numero_2, numero_3):
    numeros = [numero_1, numero_2, numero_3]
    saca_numero = 0
    if numero_1 + numero_2 + numero_3 > 15:
        for numero in numeros:
            if numero > numero:
                saca_numero = numero
        print("Condicion 1")
    elif numero_1 + numero_2 + numero_3 < 10:
        for numero in numeros:
            if numero > saca_numero:
                saca_numero = numero
        print("Condicion 2")
    else:
        for numero in numeros:
            if numero > saca_numero:
                saca_numero = numero
        print("Condicion 3")
    return saca_numero

numero_1 = input("Escribe el número 1: ")
numero_2 = input("Escribe el número 2: ")
numero_3 = input("Escribe el número 3: ")

print(devolver_distintos(int(numero_1), int(numero_2), int(numero_3)))

prueba1 = 5
prueba2 = 10
prueba3 = 15

