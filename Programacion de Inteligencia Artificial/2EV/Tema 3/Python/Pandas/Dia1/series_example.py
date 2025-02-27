import pandas as pd

# Serie desde una lista
lista = [10, 20, 30, 40]
serie1 = pd.Series(lista)
print("Serie desde lista:\n", serie1)

# Serie desde un diccionario
diccionario = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
serie2 = pd.Series(diccionario)
print("\nSerie desde diccionario:\n", serie2)

# Serie con valores personalizados
valores = [3.5, 7.8, 1.2]
indices = ['x', 'y', 'z']
serie3 = pd.Series(valores, index=indices)
print("\nSerie con valores personalizados:\n", serie3)








