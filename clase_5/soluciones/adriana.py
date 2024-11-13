num = int(input("cuantos estudiantes vas a ingresar?: "))

for _ in range(0, num):
    nombre_estudiante= input('Ingrese el nombre del estudiante: ')
    notas=(input('Ingrese las tres notas separadas por espacio: ').split())
    notas=[float(nota) for nota in notas]
    promedio= sum(notas)/ len(notas)
    if   90 <= promedio <= 100:  calificación ='Superior'
    elif 80 <= promedio <= 89: calificación ='Alto'
    elif 70 <= promedio <= 79: calificación ='Básico'
    elif 60 <= promedio <= 69: calificación ='Bájo'
    elif  0 <= promedio <= 59: calificación ='Insuficiente'
    print(f'nombre:{nombre_estudiante},promedio:{promedio},calificación:{calificación}')