import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("data.csv")

# Verificar el contenido del DataFrame
print("Contenido del Dataframe:\n", df)
print("\nInformación del DataFrame:\n", df.info())

# Ejemplo con parámetros
df = pd.read_csv("data2.csv", sep=";", usecols=["Nombre", "Ciudad"])

print("Contenido del Dataframe:\n", df)
print("\nInformación del DataFrame:\n", df.info())