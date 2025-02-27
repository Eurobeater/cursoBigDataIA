import pandas as pd

# Crear un DataFrame de ejemplo
data = {
	    "Producto": ["Manzanas", "Plátanos", "Naranjas", "Peras"],
	    "Precio": [1.2, 0.8, 1.5, 1.3],
	    "Stock": [100, 150, 120, 90]
}

df = pd.DataFrame(data)
print("DataFrame original:\n", df)

# Aplicar funciones a filas o columnas

df["Valor Total"] = df.apply(lambda row: row["Precio"] * row["Stock"], axis=1)
print("\nDataFrame con una columna calculada\n", df)

df["Valor Total 2"] = df["Precio"] * df["Stock"]
print("\nDataFrame con una columna vectorizada:\n", df)

# Filtrar datos

    # Seleccionar productos con stock mayor a 100
productos_filtrados = df[df["Stock"] > 100]
print("\nProductos con stock mayor a 100:\n", productos_filtrados)

    # Filtrar usando múltiples condiciones
productos_condiciones = df[(df["Precio"] > 1) & (df["Stock"] < 120)]
print("\nProductos con dos condiciones:\n", productos_condiciones)

# Ordenar datos
df_ordenado = df.sort_values(by=["Stock", "Precio"], ascending=[False, True])
print("\nProductos con dos condiciones\n", df_ordenado)