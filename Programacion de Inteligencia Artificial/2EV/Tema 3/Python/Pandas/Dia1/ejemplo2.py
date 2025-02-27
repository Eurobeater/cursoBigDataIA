import pandas as pd

data = {
    "Nombre": ["Juan", "Ana", "Luis", "Carlos"],
    "Edad": [25, 30, 35, 40],
    "Ciudad": ["Madrid", "Barcelona", "Valencia", "Murcia"]
}

df = pd.DataFrame(data)
print("\nDataframe:\n", df)

# Acceder a una columna
print("\nColumna 'Edad':\n", df["Nombre"])

# Acceder a una fila
print("\nFila 1:\n", df.loc[1])

print("\nFila 1:\n", df.iloc[1])

# Acceder a un elemento
print("\nElemento en la fila 1 y columna 'Nombre':", df.at[1, "Nombre"])


data = {
    "Nombre": ["Juan", "Ana", "Luis", "Carlos", "Pedro", "Sara", "Elena", "Carmen"],
    "Edad": [25, 30, 35, 40, 45, 50, 55, 60],
    "Ciudad": ["Madrid", "Barcelona", "Valencia", "Murcia", "Sevilla", "Zaragoza", "Bilbao", "Alicante"]
}

df = pd.DataFrame(data)

print("Nuevo DataFrame:\n", df)

# Explorar un DataFrame
print("Primeras Filas:\n", df.head())
print("\nDimensiones del DataFrame:", df.shape)
