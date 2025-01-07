import pandas as pd
import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect("chinook.db")

# Cargar datos de la tabla albums
df = pd.read_sql("SELECT * FROM albums", conn)

# Verificar el contenido del DataFrame
print("Contenido del Dataframe:\n", df)

# Cerrar la conexión
conn.close()
