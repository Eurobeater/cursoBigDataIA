import pandas as pd

# Crear un DataFrame de ejemplo
data = {
    "Nombre": ["Carlos", "Ana", "Luis", "Helena"],
    "Edad": [22, 28, 30, 25],
    "Ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla"],
    "Salario": [2000, 2500, 2200, None]
}

df = pd.DataFrame(data)
print("DataFrame original:\n", df)

# Manejo de valores nulos
print("Valores nulos por columna:\n", df.isnull().sum())

# Eliminar filas con valores nulos
df_sin_nulos = df.dropna()
print("\nDataFrame sin nulos:\n", df_sin_nulos)

# Reemplazar valores nulos
df["Edad"] = df["Edad"].fillna(df["Edad"].mean())
df["Ciudad"] = df["Ciudad"].fillna(["Desconocida"])
print("\nDataFrame con valores nulos reemplazados:\n", df)

# Eliminar duplicados
df_duplicado = df._append(df.iloc[0], ignore_index=True)
print("\nDataFrame con duplicados:\n", df_duplicado)

df_sin_duplicados = df_duplicado.drop_duplicates()
print("\nDataFrame sin duplicados:\n", df_sin_duplicados)

#Cambiar el tipo de datos

df["Edad"] = df["Edad"].astype(int)
print("\nDataFrame con tipo de datos cambiados:\n", df)

# Corregir valores incorrectos
df.loc[df["Edad"] > 100, "Edad"] = df["Edad"].mean().round()
print("\nDataFrame con valores incorrectos corregidos:\n", df)

# Eliminar columnas innecesarias
df_sin_salario = df.drop(columns=["Salario"])
print("\nDataFrame sin la columna Salario\n", df_sin_salario)