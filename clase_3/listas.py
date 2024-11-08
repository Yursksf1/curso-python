nombre = "Yurley"
segundo_nombre = "Kate"

nombres = ["Yurley", "Kate"]

dias_semana = [
    "lunes", 
    "martes",
    "miercoles",
    "jueves",
    "viernes",
]
print('dias_semana:', dias_semana)

print("el dia de la semana con indice 0 es:  ", dias_semana[0])
print("el dia de la semana con indice 1 es:  ", dias_semana[1])
print("el dia de la semana con indice 3 es:  ", dias_semana[3])

dias_semana[3] = "Juernes"
print("el dia de la semana con indice 3 es:  ", dias_semana[3])

# usamos la funcion append para agregar elementos a la lista
dias_semana.append("Sabado")
dias_semana.append("Domingo")

# usamos la funcion extends para extender la lista con otra lista
dias_semana.extend(["sabado", "domingo"])


print('dias_semana:', dias_semana)
#print("'dias_semana:", dias_semana)

for atributo in dias_semana:
    print('elemento: ', atributo)

nombre_completo = 'Yurley Katterine Sanchez Florez'
#print(nombre_completo)
list_nombre = nombre_completo.split()
#print(list_nombre)
print('segundo nombre: ', list_nombre[1] )

for atributo in list_nombre:
    print('elemento: ', atributo)


'''
Ejercicio:
definir una lista con los meses,
cambiar el mes numero 11 (noviembre) por un nuevo nombre, por ejemplo Pre-Navidad
agregar un nuevo atributo a la lista, que se llame "post-Navidad"
'''


# ORDEN 
'''
para ordenar elementos de una lista usamos el metodo .sort()
'''

lista_desordenada = [1,8,1,2,6,3,5,4,2, 8,7,2,6]
print('lista_desordenada', lista_desordenada)

lista_desordenada.sort()
print('lista_ordenada', lista_desordenada)


lista_desordenada.sort(reverse=True)
print('lista_ordenada desencente', lista_desordenada)

meses_anio=["ENERO",
            "FEBRERO",
            "MARZO",
            "ABRIL",
            "MAYO",
            "JUNIO",
            "JULIO",
            "AGOSTO",
            "SEPTIEMBRE",
            "OCTUBRE",
            "NOVIEMBRE",
            "DICIEMBRE"
]
meses_anio.sort(reverse=True)
print(meses_anio)

# preguntar si un valor esta dentro de la lista
print('JUNIO' in meses_anio)
print('JUNI0' in meses_anio)

# preguntar el tamanio de la lista, con la funcion len(lista)
print(len(meses_anio))

# para sumar todos los elementos de una lista de numeros, podemos usar la funcion sum(lista)
print(sum(lista_desordenada))

# Ejercicio 2
"""
definir una lista conformada unicamente de numeros, 
con una longitud minima de 15 elementos
y deben hallar el promedio de los numeros ingresados
"""


lista_desordenada = [1,8,1,2,6,3,5,4,2, 8,7,2,6]

# contar
print("se encuentra el numero 2 ",  lista_desordenada.count(2), "veces")
print("se encuentra el numero 21 ",  lista_desordenada.count(21), "veces")

# eliminar ultimo atributo
print(lista_desordenada.pop())
print('lista_desordenada', lista_desordenada)

print(lista_desordenada.pop(1))
print('lista_desordenada', lista_desordenada)

# retorna el indice de un elemento en especifico
print(lista_desordenada.index(2))


nombres = [
    "Andrea Beatriz Amezquita Araque",
    "Antony javier Estrada Araujo",
    "Brayan Enrique Silva Marquez",
    "Carlos Andres Florez Ochoa",
    "Carolina Bastidas Rincon",
    "Daniel Camilo Orejarena Vanegas",
    "Deivert Farick Blanco Marin",
    "Didier Alexander Luengas Reyes",
]

nombre_a_buscar = "Brayan Enrique Silva Marquez"

print(nombre_a_buscar in nombres)
print(nombres.index(nombre_a_buscar))

for nombre in nombres:
    print("estoy buscando a Brayan...")
    print(nombre)

    if nombre == nombre_a_buscar:
        break
