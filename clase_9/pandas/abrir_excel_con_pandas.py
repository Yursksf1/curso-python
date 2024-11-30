
import pandas as pd

# Ruta del archivo Excel
file_path = "C:/Users/Usuario/Dev/cursos_confenalco/curso_python/clase_9/pandas/archivo.xlsx"

# Leer el archivo Excel
df = pd.read_excel(file_path)

# Mostrar el contenido
print(df.head())
