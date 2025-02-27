import pandas as pd

# Crear un DataFrame de ejemplo
data = {
    "Vendedor": ["Carlos", "Ana", "Luis", "Carlos", "Ana", "Luis", "Elena", "Carlos"],
    "Producto": ["Manzanas", "Plátanos", "Naranjas", "Peras", "Manzanas", "Plátanos", "Manzanas", "Manzanas"],
    "Cantidad": [10, 5, 8, 12, 7, 6, 15, 5],
    "Precio": [2.5, 1.8, 3.0, 2.2, 2.5, 1.8, 2.5, 3.5]
}
df = pd.DataFrame(data)
print("DataFrame inicial:\n", df)

# Agrupar por una columna y calcular la suma
cantidad_por_vendedor = df.groupby("Vendedor")["Cantidad"].sum()
print("\nCantidad de productos vendidos por vendedor:\n", cantidad_por_vendedor)

# Agrupar por dos columnas y calcular la suma
cantidad_por_vendedor_producto = df.groupby(["Vendedor", "Producto"])["Cantidad"].sum()
print("\nCantidad de productos vendidos por vendedor y producto:\n", cantidad_por_vendedor_producto)

# Aplicar múltiples operaciones
# Obtener la suma y el promedio del precio por producto
estadisticas_producto = df.groupby("Producto")["Precio"].agg(["sum", "mean", "count", "max", "min"])
print("\nEstadísticas de precio por producto:\n", estadisticas_producto)

# Filtrar grupos
# Filtrar productos cuyo total de cantidad vendida sea mayor a 10
productos_filtrados = df.groupby("Producto").filter(lambda x: x["Cantidad"].sum() > 10)
print("\nProductos con cantidad total mayor a 10:\n", productos_filtrados)

# Transformar datos
# Normalizar la cantidad por grupo de producto
df["Cantidad Normalizada"] = df.groupby("Producto")["Cantidad"].transform(lambda x: x  / x.sum())
print("\nDataFrame con cantidad normalizada por producto:\n", df)











