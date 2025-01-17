import pandas as pd

# Crear un DataFrame con datos de ventas
data = {
    "ID": [1, 2, 3, 4, 5],
    "Descripción": [
        "Producto: Manzanas, Precio: $2.50",
        "Producto: Plátanos, Precio: $1.80",
        "Producto: Naranjas, Precio: $3.00",
        "Producto: Peras, Precio: $2.20",
        "Producto: Peras, Descuento: 5%"
    ]
}
df = pd.DataFrame(data)
print("DataFrame inicial\n", df)

# Identificar filas con un patrón
df["Tiene Descuento"] = df["Descripción"].str.contains("Descuento", regex=True)
print("\nDataFrame con filas que contienen 'Descuento\n", df)

# Extraer el nombre del producto
df["Producto"] = df["Descripción"].str.extract(r"Producto:\s(\w+)")
print("\nDataFrame con columna con el producto extraído:", df)

# Extraer el precio (con formato numérico)
df["Precio"] = df["Descripción"].str.extract(r"Precio:\s\$(\d+\.\d+)")
print("\nDataFrame con columna con el precio extraído:", df)

# Reemplazo de patrones
# Eliminar el texto "Producto" de la descripción por un espacio vacío
df["Descripción Limpia"] = df["Descripción"].str.replace(r"Producto:\s", "", regex=True)
print("\nDataFrame con la descripción limpia:\n", df)

# Dividir la expresión en múltiples columnas
df_split = df["Descripción"].str.split(", ", expand=True)
print("\nDataFrame con descripción dividida en columnas\n", df_split)

# Combinar patrones complejos
# Identificar filas con precios mayores a $2.00
df["Precio Mayor a $2.00"] = df["Descripción"].str.contains(r"Precio:\s\$(2\.\d+|[3-9]\.\d+)", regex=True)