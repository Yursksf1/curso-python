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
personas = [
    {
        "nombre": "diana",
        'edad': 21,
        "amigos": [
            {
                "nombre": "sofia",
                'edad': 40
            },  
        ]
    },  
    {
        "nombre": "sofia",
        'edad': 40
    },  
    {
        "nombre": "marcos",
        'edad': 50
    },
]

persona = {
    "nombre": "Jhonathan",
    "apellido": "Ramirez",
    "edad": 31,
    "ciudad": "New York",
    "mascotas": ["Mimi", "Firulais"]
}

mensaje = """
Hola mi nombre es {0} {1}
tengo {2} de edad, 
vivo en la ciudad de {3}
tengo {4} mascotas, 
sus nombre son {5} y {6}
""".format(
    persona.get('nombre'),
    persona.get('apellido'),
    persona.get('edad'),
    persona.get('ciudad'),
    len(persona.get('mascotas')),
    persona.get('mascotas')[0],
    persona.get('mascotas')[1],
)

print(mensaje)

print("-------- imprimir el diccionarios ------ ")

for key, value in persona.items():
    
    print(key, value)