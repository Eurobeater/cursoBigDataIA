import pandas as pd
import os

# Cargar el archivo Excel
# df = pd.read_excel("data.xlsx", sheet_name="Hoja1")

# Verificar el contenido del DataFrame
# print("Contenido del Dataframe:\n", df)

# Cargar otra hoja Excel
# df2 = pd.read_excel("data.xlsx", sheet_name="Hoja2")

# print("Contenido del Dataframe:\n", df2)


# Verifica el directorio actual
print("Directorio actual:", os.getcwd())

# Ruta absoluta al archivo Excel
excel_path = r"C:\Users\Eurobeater\Documents\Curso IA y Big Data Git\Programacion de Inteligencia Artificial\2EV\Python - Pandas\Dia2\data.xlsx"

# Verifica las hojas disponibles
excel_file = pd.ExcelFile(excel_path)
print("Hojas en el archivo:", excel_file.sheet_names)

# Cargar las hojas
df = pd.read_excel(excel_path, sheet_name="Hoja1")
print("Contenido de Hoja1:\n", df)

df2 = pd.read_excel(excel_path, sheet_name="Hoja2")
print("Contenido de Hoja2:\n", df2)
