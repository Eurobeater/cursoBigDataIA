from time import strftime

import pandas as pd
import numpy as np

# Crear un DataFrame con datos de ventas
data = {
    "ID": range(1, 10001),
    "Producto": np.random.choice(["Manzanas", "Plátanos", "Naranjas", "Peras"], size=10000),
    "Cantidad": np.random.randint(1, 100, size=10000),
    "Precio": np.random.uniform(1.0, 10.0, size=10000),
    "Fecha": pd.date_range(start="2023-01-01", periods=10000, freq="H").strftime("%Y-%m-%d")
}
df = pd.DataFrame(data)
print("DataFrame simulado\n", df)

# Medir el uso de memoria
print("\nUso de memoria del DataFrame")
print(df.memory_usage(deep=True))

print("\nUso de memoria del DataFrame", df.memory_usage(deep=True) / 1024 , "KB")
print("Información general:\n", df.info())

# Reducir el tamaño de los datos
# Reducir el tamaño de las columnas numéricas
print("\nDataFrame con columnas numéricas reducidas\n")
df["ID"] = df["ID"].astype(np.uint16)
df["Cantidad"] = df["Cantidad"].astype("int32")
df["Precio"] = df["Precio"].astype("float32")

print("\nUso de memoria del DataFrame\n", df.memory_usage())
print("Información general\n", df.info())

# Reducir el tamaño de las columnas categógicas
# Convertir la columna 'Producto' a tipo categórico
df["Producto"] = df["Producto"].astype("category")

print("\nUso de memoria del DataFrame", df.memory_usage(deep=True) / 1024, "KB")
print("Información general:\n", df.info())

# Convertir la columna 'Fecha' a tipo datetime
df["Fecha"] = pd.to_datetime(df["Fecha"])
print("\nUso de memoria del DataFrame", df.memory_usage(deep=True) / 1024, "KB")

# Verificar el uso de memoria reducido
print("\nUso de memoria del DataFrame:")
print(df.memory_usage(deep=True) / 1024, "KB")

# Procesamiento en fragmentos
# Leer un archivo CSV en fragmentos
chunk_size = 1000
for chunk in pd.read_csv("data\Titanic-Dataset.csv"):
    print(chunk.head())

# Uso de usecols y dtype en pd.read_csv
# Leer solo algunas columnas y especificar tipos de datos
df_optimized = pd.read_csv(
    "data\Titanic-Dataset.csv",
    usecols=["PassengerId", "Survived", "Pclass", "Name", "Fare"],
    dtype = {"Survived": "category", "Pclass": "category", "Fare": "float32"}
)
print("DataFrame optimizado:\n", df_optimized)
print("Información general:\n", df_optimized.info())