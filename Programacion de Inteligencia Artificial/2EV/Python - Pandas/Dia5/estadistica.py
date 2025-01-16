import pandas as pd
import seaborn as sn
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