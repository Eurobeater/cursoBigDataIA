import pandas as pd

# Crear una serie desde una lista
data = [10, 20, 30, 40]
series = pd.Series(data)
print("Serie:\n ", series)

# Personalizar los índices
custom_series = pd.Series(data, index=['a', 'b', 'c', 'd'])
print("\nSerie con índices personalizados:\n", custom_series)

# Acceder a elementos de la serie
print("\nElemento en el índice b:", custom_series['b'])