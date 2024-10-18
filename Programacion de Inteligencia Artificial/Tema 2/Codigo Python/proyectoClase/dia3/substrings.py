texto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
fragmento = texto[2]
print(fragmento)

fragmento = texto[2:5]      #No se incluyo el último
print(fragmento)

fragmento = texto[15:]
print(fragmento)

fragmento = texto[:5]
print(fragmento)

fragmento = texto[2:10:2]   #Empieza en 2, termina en 10 y va de 2 en 2. Este ultimo se llama salto
print(fragmento)

fragmento = texto[::3]      #Salta de 3 en 3
print(fragmento)

fragmento = texto[::-1]     #Escribe del revés la cadena porque no le he puesto inicio final. Salta de 1 en 1
print(fragmento)

fragmento = texto[::-1]     #Escribe del revés la cadena porque no le he puesto inicio final. Salta de 2 en 2
print(fragmento)