import csv

# Ruta del archivo
file_path = "C:/Users/Usuario/Dev/cursos_confenalco/curso_python/clase_9/archivo_csv/archivo.csv"

# Leer el archivo CSV
with open(file_path, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    suma = 0
    contador = 0
    for row in reader:
        print(row)
        suma = suma + int(row[1])
        contador = contador + 1 
    print('total:', suma)
    print('prodmedio:', suma/contador)