import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Crear un DataFrame con datos de ventas
data = {
    "Producto": ["Manzanas", "Manzanas", "Naranjas", "Peras", "Peras", "Naranjas", "Manzanas"],
    "Ventas": [100, 120, 90, 110, 150, 130],
    "Precio": [2.5, 2.5, 3.0, 2.2, 2.2, 3.0, 2.5],
    "Descuento": [50, 70, 60, 40, 55, 65, 45],
    "Stock": [50, 70, 60, 40, 55, 65, 45]
}
df = pd.DataFrame(data)
print("DataFrame inicial\n", df)

# Calcular correlaciones
correlation_matrix= df.corr()
print("\nMatriz de correlación\n", correlation_matrix)

# AQUI FALTA ALGO ###############################################

# Análisis estadístico
# Coeficiente de correlación de
from scipy.stats import pearsonr

# Calcular el coeficiente de correlación
corr, p_value = pearsonr(df["Precio"], df["Ventas"])
print("\nCoeficiente de correlación de Pearson entre precio y ventas", corr)
print("p-Valor:", p_value)

# Relación categórica
# Relación entre producto y ventas
plt.figure(figsize=(8, 6))
sns.barplot(x="Producto", y="Ventas", data=df, palette="Set2")
plt.title("Ventas por producto", fontsize=16)
plt.xlabel("Producto", fontsize=12)
plt.ylabel("Ventas", fontsize=12)
plt.show()