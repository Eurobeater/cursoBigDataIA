def multiplicar(numero1, numero2):
    return numero1 * numero2

resultado = multiplicar(5, 5)
print(resultado)

resultado = multiplicar(2.5, 3.12)
print(resultado)

print(multiplicar('Hola ', 3))      # Imprime Hola 3 veces

#resultado = multiplicar('Hola ', 'Mundo')
#print(resultado)
# Error

def invertir_palabra(palabra):
    return palabra[::-1].upper()

print(invertir_palabra('Hola'))