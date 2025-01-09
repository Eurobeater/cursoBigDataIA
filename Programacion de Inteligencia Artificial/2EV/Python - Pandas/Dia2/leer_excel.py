import pandas as pd

# Cargar el archivo Excel
df = pd.read_excel("data.xlsx", sheet_name="Hoja1")

# Verificar el contenido del DataFrame
print("Contenido del Dataframe:\n", df)

# Cargar otra hoja Excel
df2 = pd.read_excel("data.xlsx", sheet_name="Hoja2")

print("Contenido del Dataframe:\n", df2)