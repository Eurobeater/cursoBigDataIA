import pandas as pd

# Crear un DataFrame con datos de ventas
data = {
    "Fecha": ["2023-01-01", "2023-01-03", "2023-01-07", "2023-01-10"],
    "Vendedor": ["Carlos", "Ana", "Luis", "Carlos"],
    "Ventas": [100, 150, 200, 130]
}
df = pd.DataFrame(data)
print("DataFrame inicial:\n", df)
print("Información general:\n", df.info())

# Convertir la columna 'Fecha' a tipo datetime
df["Fecha"] = pd.to_datetime(df["Fecha"])
print("DataFrame con fechas convertidas:\n", df)
print("Información general:\n", df.info())

# Obtener el día, mes y año de la fecha
df["Año"] = df["Fecha"].dt.year
df["Mes"] = df["Fecha"].dt.month
df["Día"] = df["Fecha"].dt.day

print("DataFrame con columnas de año, mes y día:\n", df)
print("Información general:\n", df.info())

# Obtener el día de la semana
df["Día semana"] = df["Fecha"].dt.day_name()
print("DataFrame con columnas de año, mes y día:\n", df)

# Filtrar y seleccionar por fechas
# filtrar ventas posteriores al 2023-01-05

ventas_posteriores = df[df["Fecha"] > "2023-01-05"]
print("Ventas posteriores a 2023-01-05:\n", ventas_posteriores)

# Filtrar por un rango de fechas
ventas_rango = df[(df["Fecha"] >= "2023-01-01") & (df["Fecha"] <= "2023-01-07")]
print("Ventas en el rango 2023-01-01 a 2023-01-07:\n", ventas_rango)

# Generar rangos de fechas
rango_fechas = pd.date_range(start="2023-01-01", end="2023-01-10", freq="D")
print("Rango de fechas:\n", rango_fechas)

# Operaciones con fechas
df["Días desde inicio"] = (df["Fecha"] - df["Fecha"].min()).dt.days
print("DataFrame con diferencia de días:\n", df)






