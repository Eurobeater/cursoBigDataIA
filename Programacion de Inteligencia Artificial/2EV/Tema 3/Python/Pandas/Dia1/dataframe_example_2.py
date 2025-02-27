import pandas as pd

data = {
    "Producto": ["Manzanas", "Plátanos", "Naranjas", "Peras"],
    "Precio": [1.2, 0.8, 1.5, 1.3],
    "Stock": [100, 150, 120, 90]
}
df = pd.DataFrame(data, index=["A", "B", "C", "D"])
print("DataFrame:\n", df)

# Ejemplos de uso de .loc[]
# Seleccionar una fila por etiqueta
print("Fila B:\n", df.loc["B"])

# Seleccionar la columna "Producto"
print("Columna Producto:\n", df.loc[:, "Producto"])

# Seleccionar un valor específico
print("Precio de las Naranjas:\n", df.loc["C", "Precio"])

# Ejemplos de uso de .iloc[]
# Seleccionar una fila por posición
print("Fila 2:\n", df.iloc[1])

# Seleccionar una columna por posición
print("Columna 3 (stock):\n", df.iloc[:, 2])

# Seleccionar un valor específico
print("Precio de las Naranjas:\n", df.iloc[2,1])









