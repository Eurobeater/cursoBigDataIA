import pandas as pd

# Crear un DataFrame de ejemplo
data = {
	    "Producto": ["Manzanas", "Plátanos", "Naranjas", "Peras"],
	    "Precio": [1.2, 0.8, 1.5, 1.3],
	    "Stock": [100, 150, 120, 90]
}

df = pd.DataFrame(data)
print("DataFrame original:\n", df)

# Configurar un indice

df_indexado = df.set_index("Producto")
print("DataFrame indexado:\n", df_indexado)

# Convertir el indice en una columna
df_reset = df_indexado.reset_index()
print("DataFrame reseteado:\n", df_reset)

# Modificar las etiquetas
df_indexado.index = ["A", "B", "C", "D"]
print("DataFrame con índice modificado:\n", df_indexado)

df_reset = df_indexado.reset_index()
print("DataFrame reseteado:\n", df_reset)

# Acceso y seleccion de datos usando indices
fila = df_indexado.loc["A"]
print("Fila con índice A\n", fila)

varias_filas = df_indexado.loc[["A", "C"]]
print("Filas seleccionadas:\n", varias_filas)

# Índices jerárquicos
multi_index = pd.MultiIndex.from_tuples(
    [("Frutas", "Manzanas"), ("Frutas", "Platanos"), ("Frutas", "Naranjas"), ("Frutas", "Peras")],
    names = ["Categoria", "Producto"]
)
df_multi = pd.DataFrame(data, index=multi_index).drop(columns="Producto")
print("DataFrame con indices jerárquicos:\n", df_multi)