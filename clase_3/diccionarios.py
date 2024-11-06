# estructuras de {llave: valor}

my_diccionario = {
    "nombre": "Yurley",
    "apellido": "Sanchez",
    "edad": 35,
}

print('my_diccionario', my_diccionario)
print(my_diccionario['edad'])
print(my_diccionario.get('edad'))

print(my_diccionario.get('edadd'))
#print(my_diccionario['edadd'])
print(my_diccionario.keys())
print(my_diccionario.values())
print(my_diccionario.items())

# ejercicio
'''
 definir un diccionario en python que contenga las llaves de:
 nombre, apellido, 
 edad, ciudad, 
 nombre de las mascotas, 

 imprimir un mensaje de saludo que contenga la siguiente estructura:
 Hola mi nombre es Juan Diaz, tengo 28 de edad, vivo en la ciudad de New York
 tengo 2 mascotas, sus nombre son Mimi y Firulais
'''