opcion_usuario = 0

def saludar():
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@ Bienvenido, usuario @@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("")

def terminar_programa():
    print("")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@ Hasta la próxima @@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

def listar_opciones():
    opcion1 = "Opcion 1"
    opcion2 = "Opcion 2"
    opcion3 = "Opcion 3"
    opcion4 = "Opcion 4"
    opcion5 = "Opcion 5"
    opcion6 = "Opcion 6"

    print("******** Elige una opción **********")
    print(f"- {opcion1}")
    print(f"- {opcion2}")
    print(f"- {opcion3}")
    print(f"- {opcion4}")
    print(f"- {opcion5}")
    print(f"- {opcion6}")

saludar()

while opcion_usuario != 6:
    listar_opciones()
    opcion_usuario = int(input("Elige una opción: "))
    if opcion_usuario == 6:
        terminar_programa()



