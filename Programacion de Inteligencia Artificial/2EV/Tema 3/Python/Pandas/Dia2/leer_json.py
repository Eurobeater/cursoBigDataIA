import pandas as pd

# Cargar el archivo JSON
df = pd.read_json("data.json")

# Verificar el contenido del DataFrame
print("Contenido del Dataframe:\n", df)