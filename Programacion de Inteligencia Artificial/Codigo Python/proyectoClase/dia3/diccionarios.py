diccionario = {'c1': 'valor1', 'c2': 'valor2'}
print(type(diccionario))
print(diccionario)

resultado = diccionario['c1']       #Imprime el valor de la clave c1
print(resultado)

cliente = {'nombre': 'Juan', 'apellido': 'Fuentes', 'peso': 88, 'talla': 'X'}
consulta = cliente['apellido']
print(consulta)

#Al acceder a una clave que no existe en el diccionario, salta un error
#consulta = cliente['edad']
#print(consulta)

dic = {'c1': 55, 'c2': [10, 20, 30], 'c3': {'s1':100, 's2':200}}    #Un diccionario anidado
print(dic['c2'])
print(dic['c2'][1])     #Acceder al segundo elemento del diccionario anidado
print(dic['c3'])
print(dic['c3']['s2'])  #Igual que el anterior comentario, solo que accediendo a la clave

dic = {'c1': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}
print(dic['c2'][1].upper())

dic = {1: 'a', 2: 'b'}
print(dic)

dic[3] = 'c'    #Modificar el diccionario añadiendo una nueva clave. Los diccionarios son mutables
print(dic)

dic[2] = 'B'    #Igual que el anterior pero modificando el valor de una clave
print(dic)

print(dic.keys())           #Imprime todas las claves en formato lista (Array)
print(dic.values())         #Imprime todos los valores en formato lista (Array)
print(dic.items())          #Imprime todos las claves con sus valores en formato lista (Array)
print(type(dic.items()))    #Devuelve una  clase de tipo 'dic_items'
dicItems = dic.items()