import pandas as pd

# Ruta del archivo
file_path = "C:/Users/Usuario/Dev/cursos_confenalco/curso_python/clase_9/pandas/archivo.csv"

# Leer el archivo CSV
df = pd.read_csv(file_path)

# Mostrar el contenido
print(df.head())

