import matplotlib.pyplot as plt
import pandas as pd
from scipy.special import linestyle

# Crear un DataFrame de ejemplo
data = {
    "Producto": ["Manzanas", "Platanos", "Naranjas", "Peras"],
    "Ventas": [100, 120, 90, 110],
    "Stock": [50, 70, 60, 40],
    "Precio": [2.5, 1.8, 3.0, 2.2]
}
df = pd.DataFrame(data)
print("DataFrame inicial:\n", df)

# Crear un gráfico de barras con Matplotlib
plt.figure(figsize=(8, 5))
plt.bar(df["Producto"], df["Ventas"], color="skyblue")
plt.title("Ventas por producto", fontsize=16)
plt.xlabel("Producto", fontsize=12)
plt.ylabel("Ventas", fontsize=12)
plt.grid(axys="y", linestyle="--", alpha=0.7)
plt.show()

# Gráfico de líneas personalizado con Matplotlib
# Gráfico de líneas para ventas y stock
plt.figure(figsize=(8, 6))
plt.plot(df["Producto"], df["Ventas"], marker="o", color="blue", label="Ventas")
plt.plot(df["Producto"], df["Stock"], marker="s", color="Green", label="Ventas")
plt.title()
plt.xlabel()
plt.ylabel()
plt.legend()
plt.grid()
plt.show()

# Crear un gráfico de barras con Seaborn
plt.figure(figsize=(8, 6))
sns.barplot(x="Producto", y="Ventas", data=df, palette="Blues_d")
plt.title("Ventas por producto (Seaborn)", fontsize=16)
plt.xlabel("Producto", fontsize=12)
plt.ylabel("Ventas", fontsize=12)
plt.show()

# Gráfico de cajas. Ditribución de ventas
plt.figure(figsize=(8, 6))
sns.boxplot(x="Producto", y="Ventas", data=df, pallete="Set2")
plt.title("Distribución de ventas por producto", fontsize=16)
plt.xlabel("Producto", fontsize=16)
plt.ylabel("Ventas", fontsize=16)
plt.show()

# Gráfico combinado con Matplotlib y Seaborn
# Añadir líneas de tendencia a un gráfico de barras
plt.figure(figsize=(8, 6))
sns.barplot(x="Producto", y="Ventas", df=df, palette="coolwarm")
plt.plot(df["Producto"], df["Stock"], marker="o", color="red", label="Stock")
plt.title("Ventas y stock por producto", fontsize=16)
plt.xlabel("Producto", fontsize=12)
plt.ylabel("Cantidad", fontsize=12)
plt.legend()
plt.show()