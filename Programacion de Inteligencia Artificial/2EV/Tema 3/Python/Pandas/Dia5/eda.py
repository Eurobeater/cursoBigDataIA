import pandas as pd

# Crear un DataFrame con datos de ventas
data = {
    "Vendedor": ["Carlos", "Ana", "Luis", "Carlos", "Ana", "Luis", "Elena"],
    "Producto": ["Manzanas", "Manzanas", "Naranjas", "Peras", "Peras", "Naranjas", "Manzanas"],
    "Ventas": [100, 120, 90, 150, 200, 130, 80],
    "Fecha": ["2023-01-01", "2023-01-01", "2023-01-02", "2023-01-02", "2023-01-03", "2023-01-03", "2023-01-03"],
    "Precio": [2.5, 2.5, 3.0, 2.2, 2.2, 3.0, 2.5]
}
df = pd.DataFrame(data)
df["Fecha"] = pd.to_datetime(df["Fecha"])
print("DataFrame inicial:\n", df)

# Explorar la esctuctura y calidad de lso datos
# Verificar valores nulos y duplicados
print("Valores nulos por columna:\n", df.isnull().sum())

# Verificar valores duplicados
print("\nNúmero de filas duplicadas", df.duplicated().sum())

# Estadísticas descriptivas
# Estadísticas básicas de las columnas numéricas
print("\nEstadísticas descriptivas de columnas numéricas\n", df.describe())

# Estadísticas de las columnas categóricas
print("\nEstadísticas de columnas categóricas\n", df["Producto"].value_counts())

# Detectar patrones y relaciones
# Distribución de las ventas
import seaborn as sns
import matplotlib.pyplot as plt

# Gráfico de caja para ventas
plt.figure(figsize=(8, 6))
sns.boxplot(x="Producto", y="Ventas", data=df, palette="Set2")
plt.title("Distribución de ventas por producto", fontsize=16)
plt.xlabel("Producto", fontsize=12)
plt.ylabel("Ventas", fontsize=12)
plt.show()

# Relación entre precio y ventas
# Gráfico de dispersión para precio y ventas
plt.figure(figsize=(8, 6))
sns.scatterplot(x="Precio", y="Ventas", data=df, hue="Producto", palette="viridis", s=100)
plt.title("Relación entre precio y ventaso", fontsize=16)
plt.xlabel("Producto", fontsize=12)
plt.ylabel("Ventas", fontsize=12)
plt.show()

# Tendencias temporales
# Gráfico de líneas para ventas a lo largo del tiempo
plt.figure(figsize=(10, 6))
sns.lineplot(x="Fecha", y="Ventas", data=df, hue="Producto", palette="tab10", marker="o")
plt.title("Tendencia de ventas a lo largo del tiempo", fontzise=16)
plt.title("Relación entre precio y ventaso", fontsize=16)
plt.xlabel("Fecha", fontsize=12)
plt.ylabel("Ventas", fontsize=12)
plt.show()
