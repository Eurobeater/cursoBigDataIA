import pandas as pd

# Crear un DataFrame
data = {
    "Nombre": ["Carlos", "Ana", "Luis", "Helena"],
    "Edad": [22, 28, 30, 25],
    "Ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla"],
    "Salario": [2000, 2500, 2200, None]
}

df = pd.DataFrame(data)

# Estadisticas descriptivas para columnas numéricas
print("\nEstadísticas descriptivas para columnas numéricas:\n", df.describe())

# Estadisticas descriptivas para columnas categóricas
print("\nEstadísticas descriptivas para columnas categóricas:\n", df.describe(include='object'))