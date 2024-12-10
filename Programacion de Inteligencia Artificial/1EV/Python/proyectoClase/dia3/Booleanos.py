var1 = True
var2 = False
print(type(var1))
print(type(var2))
print(var1)
print(var2)

numero = 5 > 2 + 3      #Devuelve False
print(type(numero))
print(numero)

numero = 5 >= 2 + 3     #Devuelve True
print(type(numero))
print(numero)

numero = 5 != 2 + 3     #Devuelve False
print(type(numero))
print(numero)

numero = bool(5 >6)      #Devuelve False
print(type(numero))
print(numero)

print(bool())           #Devuelve False
print(bool(0))          #Devuelve False
print(bool(''))         #Devuelve False

lista = [1, 2, 3, 4]
control = 5 in lista
print(type(control))    #Devuelve tipo bool
print(control)          #Devuelve False