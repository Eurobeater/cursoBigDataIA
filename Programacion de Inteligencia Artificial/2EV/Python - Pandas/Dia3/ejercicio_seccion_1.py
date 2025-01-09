import pandas as pd

data = {
    "Nombre": ["Juan", "Ana", "Luis", "Carlos"],
    "Edad": [25, 30, 35, 40],
    "Ciudad": ["Madrid", "Barcelona", "Valencia", "Murcia"]
}

df = pd.DataFrame(data)

df_renombrado = df.rename(columns = {"Nombre": "Empleado", "Ciudad": "Ubicacion"})
print(df_renombrado)

df["Salario"] = df["Edad"] * df["Edad"]
print("\nDataFrame con una columna calculada\n", df)

df["Estado"] = "Activo"
print("\nDataFrame con una columna de valor fijo\n", df)

df_sin_estado = df.drop(columns=["Estado"])
print("\nDataFrame con una columna menos:\n", df_sin_estado)

data = {
	    "Producto": ["Manzanas", "Plátanos", "Naranjas", "Peras"],
	    "Costo": [1.2, 0.8, 1.5, 1.3],
	    "Cantidad": [100, 150, 120, 90]
}

df = pd.DataFrame(data)

df_renombrado = df.rename(columns = {"Costo": "Precio Unitario"})
print("\n", df_renombrado)

df["Stock Total"] = df["Costo"] * df["Cantidad"]
print("\nDataFrame con una columna calculada\n", df)

df_sin_estado = df.drop(columns=["Cantidad"])
print("\nDataFrame con una columna menos:\n", df_sin_estado)