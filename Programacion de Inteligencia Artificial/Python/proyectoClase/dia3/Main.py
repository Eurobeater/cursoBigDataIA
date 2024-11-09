nombre = input("Dime tu nombre ")
monto = input("Introduce el monto ")

monto = int(monto)
comision = (monto * 13) / 100

print(f"La comision de {nombre} es: " +str(comision))