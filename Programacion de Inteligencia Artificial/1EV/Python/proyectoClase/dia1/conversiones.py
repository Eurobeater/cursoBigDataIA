num1 = 20
num2 = 30.5

#Conversion implícita
num = num1 + num2
print(num)
print(type(num))
print(type(num1))
print(type(num2))


#Conversion explícita
num1 = 5.8
print(num1)
print(type(num1))

num2 = int(num)
print(num2)
print(type(num2))

edad = input("Dime tu edad ")
print("Tu edad es " + edad)
print(type(edad))
edad = int(edad)
nuevaEdad = edad + 1
print(type(nuevaEdad))

#print("Tu edad dentro de un año sera " + nuevaEdad)
print("Tu edad dentro de un año sera " + str(nuevaEdad))