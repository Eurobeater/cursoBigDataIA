import pandas as pd

# Crear un DataFrame
data = {
    "Nombre": ["Carlos", "Ana", "Luis", "Helena"],
    "Edad": [22, 28, 30, 25],
    "Ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla"],
    "Salario": [2000, 2500, 2200, None]
}

df = pd.DataFrame(data)

# Ver las primeras filas
print("Primeras filas del DataFrame:\n", df.head())

# Ver las ultimas filas
print("Últimas filas del DataFrame:\n", df.tail())

# Ver informacion general del DataFrame
print("\nInformación del DataFrame:")
print(df.info())

# Dimensiones del DataFrame
print("\nDimensiones del DataFrame:", df.shape)

# Nombres de las columnas
print("\nNombres de las columnas:", df.columns)

# Tipos de datos de cada columna
print("\nTipos de datos de cada columna:\n", df.dtypes)
