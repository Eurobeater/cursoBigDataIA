import pandas as pd

# Crear un DataFrame de ejemplo
data = {
    "Producto": ["Manzanas", "Platanos", "Naranjas", "Peras"],
    "Ventas": [100, 120, 90, 110],
    "Stock": [50, 70, 60, 40],
    "Precio": [2.5, 1.8, 3.0, 2.2]
}

df = pd.DataFrame(data)
print("DataFrame inicial:\n", df)

# Visualizar las ventas de los productos. Gráfico de líneas
df.plot(kind="line", x="Producto", y="Ventas", title="Ventas por producto", xlabel="Producto", ylabel="Ventas")
plt.show()

# Visualizar las ventas de los productos. Gráfico de barras
df.plot(kind="bar", x="Producto", y=["Ventas", "Stock"], title="Ventas y stock por producto", xlabel="Producto", ylabel="Ventas")
plt.show()

# Gráfico de barras horizontales
df.plot(kind="barh", x="Producto", y="Precoi", title="Precio por producto", xlabel="Precio", ylabel="Ventas")
plt.show()

# Histograma
df["Precio"].plot(kind="hist", binds=5, tittle="Distribución del precio", xlabel="Producto")
df.plot(kind="barh", x="Producto", y="Precio", tittle="Precio por producto", xlabel="Precio", ylabel="Ventas")

# Gráfico de dispersión
df.plot(kind="scatter", x="Prrecio", y="Ventas", tittle="Relación entre precio y ventas", xlabel="Precio", ylabel="Ventas")
plt.show()

# Proporción de ventas por producto. Gráfico de tarta
df.set_index("producto")["ventas"].plot(kind="pie", autopct="%1.1f%%", title = "")