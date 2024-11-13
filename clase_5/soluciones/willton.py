
print(""" 3-)	Una institución educativa utiliza el siguiente sistema de calificaciones para evaluar el desempeño de sus estudiantes:
●	Superior: 90 - 100
●	Alto: 80 - 89
●	Básico: 70 - 79
●	Bajo: 60 - 69
●	Insuficiente: 0 - 59
""")

# Función para asignar la calificación
def asignar_calificacion(promedio):
    if promedio >= 90:
        return "Superior"
    elif promedio >= 80:
        return "Alto"
    elif promedio >= 70:
        return "Básico"
    elif promedio >= 60:
        return "Bajo"
    else:
        return "Insuficiente"


#ENCABEZADO
print("{:<10} {:<10}  {:<10} {:<10} {:<10} {:<10}".format("Nombre", "nota 1", "nota 2", "nota 3","promedio","Calificación"))#{:<10} esto quiere decir la alineación y espacio que ocupara como una encabezado
#IMPRIMIR VALORES
estudiantes=[]

numero_estudiantes = int(input("ingresa el numero de estudiantes: "))
porcentajes = {
    "nota1": 0.2,
    "nota2": 0.3,
    "nota3": 0.5,
}


for _ in range(numero_estudiantes):
    estudiante={}
    estudiante["nombre"]=input("Ingrese el nombre del estudiante: ")
    estudiante["nota1"]=float(input("Ingrese la primera nota: "))
    estudiante["nota2"]=float(input("Ingrese la segunda nota: "))
    estudiante["nota3"]=float(input("Ingrese la tercera nota: "))
    estudiantes.append(estudiante)
    print("-"*30) #separador

for estudiante in estudiantes:
    promedio = (
        estudiante["nota1"] * porcentajes.get("nota1")
        + estudiante["nota2"] * porcentajes.get("nota2")
        + estudiante["nota3"] * porcentajes.get("nota3")
        )   # Cálculo del promedio
    calificacion=asignar_calificacion(promedio)
    print()
    print(f"Nombre: {estudiante['nombre']}")
    print(f"Nota 1: {estudiante['nota1']}")
    print(f"Nota 2: {estudiante['nota2']}")
    print(f"Nota 3: {estudiante['nota3']}")
    print(f"Promedio: {promedio:.1f}")
    print(f"Calificaión: {calificacion}")    
    print("-" * 30)  # Separador entre estudiantes







