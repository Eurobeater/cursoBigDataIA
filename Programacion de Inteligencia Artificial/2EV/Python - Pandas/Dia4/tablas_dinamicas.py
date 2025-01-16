import pandas as pd

# Crear un DataFrame con datos de ventas
data = {
    "Vendedor": ["Carlos", "Ana", "Luis", "Carlos", "Ana", "Luis", "Elena"],
    "Producto": ["Manzanas", "Manzanas", "Naranjas", "Peras", "Peras", "Naranjas", "Manzanas"],
    "Ventas": [100, 120, 90, 150, 200, 130, 80],
    "Fecha": ["2023-01-01", "2023-01-01", "2023-01-02", "2023-01-02", "2023-01-03", "2023-01-03", "2023-01-03"]
}
df = pd.DataFrame(data)
df["Fecha"] = pd.to_datetime(df["Fecha"])
print("DataFrame inicial:\n", df)

# Crear una tabla dinámica básica. Resumir ventas por producto
pivot = df.pivot_table(values="Ventas", index="Producto", aggfunc="sum")
print("\nTabla dinámica de ventas por producto:\n", pivot)

# Usar múltiples índices o columnas. Resumir ventas por producto y vendedor
pivot_multi = df.pivot_table(values="Ventas", index=["Producto", "Vendedor"], aggfunc="sum")
print("\nTabla dinámica de ventas por producto y vendedor:\n", pivot_multi)

# Usar columnas y totales.
pivot_col = df.pivot_table(values="Ventas", index="Producto", columns="Vendedor", aggfunc="sum", margins=True, fill_value=0)
print("\nTabla dinámica de ventas por producto y vendedor con totales:\n", pivot_col)

# Tablas dinámicas con múltiples funciones. Calcular suma y promedio por producto
pivot_multi_agg = df.pivot_table(values="Ventas", index="Producto", aggfunc=["sum", "mean"])
print("\nTabla dinámica de ventas por producto con suma y promedio:\n", pivot_multi_agg)

# Tablas dinámicas por periodos de tiempo.
# Agrupar por día
pivot_fecha = df.pivot_table(values="Ventas", index=df["Fecha"].dt.to_period("D"), aggfunc="sum")
print("\nTabla dinámica de ventas por día:\n", pivot_fecha)









