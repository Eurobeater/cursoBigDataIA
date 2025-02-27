import pandas as pd

# Crear un DataFrame de ejemplo

data = {
    "Producto": ["Manzanas", "Plátanos", "Naranjas", "Peras"],
    "Precio": [1.2, 0.8, 1.5, 1.3],
    "Stock": [100, 150, 120, 90]
}
df = pd.DataFrame(data)
print("DataFrame original:\n", df)

# Renombrar columnas
df_renombrado = df.rename(columns = {"Producto": "Nombre", "Stock": "Inventario"})
print("\nDataFrame con columnas renombradas\n", df_renombrado)

df.columns = ["Item", "Coste", "Cantidad"]
print("\nDataFrame con todos los nombres de columnas cambiados\n", df)

# Añadir columnas nuevas
df["Valor Total"] = df["Coste"] * df["Cantidad"]
print("\nDataFrame con una columna calculada\n", df)

df["Categoria"] = "Fruta"
print("\nDataFrame con una columna de valor fijo\n", df)

# Eliminar columnas
df_sin_categoria = df.drop(columns=["Categoria"])
print("\nDataFrame con una columna menos:\n", df_sin_categoria)

# Modificar valores en una columna
df["Item"] = df["Item"].apply(lambda x: x.upper())
print("\nDataFrame con una columna modificada:\n", df)

