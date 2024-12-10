# Los decoradores son funciones que reciben una función como argumento
# y devuelven otra función.
# Se utilizan para modificar el comportamiento de
# una función sin modificar su código.

def mayuscula(texto):
    print(texto.upper())

def minuscula(texto):
    print(texto.lower())

# Si queremos imprimir un mensaje antes y después de la función
print("Hola")
mayuscula("Hoy es un buen día")
print("Adiós")

# Una alternativa para hacer lo mismo es incluir un mensaje en la propia función
def mayuscula2(texto):
    print("Hola")
    print(texto.upper())
    print("Adiós")

def minuscula2(texto):
    print("Hola")
    print(texto.lower())
    print("Adiós")

# Podemos definir una función cuyo argumento sea otra función
def una_funcion(funcion):
    return funcion

una_funcion(mayuscula("Hola1"))
una_funcion(mayuscula)("Hola2")     # Lo mismo pero poner los parámetros fuera de la función una_funcion()

# Decoradores
# Un decorador es una función que recibe una función como argumento
# y devuelve otra función

def decorar_saludo(funcion):
    def otra_funcion():
        print("Hola")
        funcion()
        print("Adiós")
    return otra_funcion

# Para decorar una función, se pone el decorador encima de la función
@decorar_saludo
def mayuscula4(texto):
    print(texto.upper())

@decorar_saludo
def minuscula4(texto):
    print(texto.lower())

mayuscula4('Python')
minuscula4('Python')

# Pero lo anterior hará que siempre aparezca la función
# decorada con los mismos saludos.

# Si queremos que unas veces salude y otras no, podemos
# hacer que el decorador reciba un argumento.

def mayuscula5(texto):
    print(texto.uper())

def minuscula5(texto):
    print(texto.lower())

mayuscula5('Python')
minuscula5('Python')

# Para que salude
decorar_saludo(mayuscula5('Python'))
decorar_saludo(minuscula5('Python'))