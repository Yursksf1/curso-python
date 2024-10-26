"""
Marcos trabajó 50 horas, con un salario de $11,500 por hora.
Juan trabajó 9 horas a la semana durante 8 semanas, con un valor de $35,200 por hora.
Stefany trabajó 4 horas diarias durante 30 días, con un valor de $25,000 por hora.


Crea un programa en Python que permita calcular el monto total a pagar a  un empleados. 
El programa debe solicitar al usuario el número de horas trabajadas y el valor por hora, 
y luego debe mostrar el total a pagar.
"""

marcos = 50 * 11500
print(f'a marcos se le debe paga: {marcos}')

juan = 9 * 8 * 35200
print(f'a juan se le debe paga: {juan}')

num_horas = int(input("Ingresa el numero de Horas: "))
valor_hora = int(input("Ingresa el valor que se debe pagar por cada Hora: "))
print(f"el valor a pagar sera de: {num_horas*valor_hora}")