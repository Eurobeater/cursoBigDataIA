import pandas as pd

# DataFrame desde un diccionario de listas
data = {
    "Nombre": ["Juan", "Ana", "Luis", "Carlos"],
    "Edad": [25, 30, 35, 40],
    "Ciudad": ["Madrid", "Barcelona", "Valencia", "Murcia"]
}

df1 = pd.DataFrame(data)
print("\nDataframe desde un diccionario de listas:\n", df1)

# DataFrame desde una lista de diccionarios
data = [
    {"Nombre": "Juan", "Edad": 25, "Ciudad": "Madrid"},
    {"Nombre": "Ana", "Edad": 30, "Ciudad": "Barcelona"},
    {"Nombre": "Luis", "Edad": 35, "Ciudad": "Valencia"},
    {"Nombre": "Carlos", "Edad": 40, "Ciudad": "Murcia"}
]
df2 = pd.DataFrame(data)
print("\nDataframe desde una lista de diccionarios:\n", df2)

# Seguimos con la exploración de un DataFrame
print("Primeras Filas:\n", df2.head())
print("\nDimensiones del DataFrame:\n", df2.shape)
print("\nNombres de las columnas:\n", df2.columns)
print("\nTipos de datos de cada columna:\n", df2.dtypes)
print("\nInformación del DataFrame:\n", df2.info())





