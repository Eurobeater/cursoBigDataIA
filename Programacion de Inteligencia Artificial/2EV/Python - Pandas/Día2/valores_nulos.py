import pandas as pd

# Crear un DataFrame
data = {
    "Nombre": ["Carlos", "Ana", "Luis", "Helena"],
    "Edad": [22, 28, 30, 25],
    "Ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla"],
    "Salario": [2000, 2500, 2200, None]
}

df = pd.DataFrame(data)

# Identificar valores nulos
print("\nValores nulos en el DataFrame:\n", df.isnull())

# Contar valores nulos por columna
print("\nValores nulos por columna:\n", df.isnull().sum())

# en todo el DataFrame
print("\n en todo el DataFrame:\n", df.isnull().any().any())