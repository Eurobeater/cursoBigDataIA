import pandas as pd

# Crear el primer DataFrame
df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Nombre": ["Carlos", "Ana", "Luis"],
    "Edad": [30, 25, 28]
})

# Crear el segundo DataFrame
df2 = pd.DataFrame({
    "ID": [2, 3, 4],
    "Ciudad": ["Madrid", "Barcelona", "Valencia"],
    "Salario": [3000, 3200, 2800]
})

print("DataFrame 1:\n", df1)
print("\nDataFrame 2:\n", df2)

# Concatenación por filas (por defecto)
df_concat = pd.concat([df1, df2], ignore_index=True)
print("\nConcatenación por filas:\n", df_concat)

# Concatenación por columnas
df_concat_cols = pd.concat([df1, df2], axis=1)
print("\nConcatenación por columnas:\n", df_concat_cols)

# Combinación
# Inner join (por defecto)
df_inner = pd.merge(df1, df2, on="ID", how="inner")
print("\nInner join:\n", df_inner)

# Left join
df_left = pd.merge(df1, df2, on="ID", how="left")
print("\nLeft join:\n", df_left)

# Right join
df_right = pd.merge(df1, df2, on="ID", how="right")
print("\nRight join:\n", df_right)

# Outer join
df_outer = pd.merge(df1, df2, on="ID", how="outer")
print("\nOuter join:\n", df_outer)

# Union por índices
# Crear un índice y unir
df1_indexed = df1.set_index("ID")
df2_indexed = df2.set_index("ID")
df_union = df1_indexed.join(df2_indexed, how="inner")
print("\nUnión por índices:\n", df_union)









