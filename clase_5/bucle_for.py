# listas y tuplas
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print ("Hoy quiero comer: ", fruta)

colores = ("rojo", "verde", "azul")
for color in colores:
    print(color)

# rangos
for numero in range(5):
    print(numero)

for numero in range(10, 25):
    print(numero)

for numero in range(10, 50, 2):
    print(numero)


# diccionarios 
persona = {
    "nombre": "Jhonathan",
    "apellido": "Ramirez",
    "edad": 31,
    "ciudad": "New York",
    "mascotas": ["Mimi", "Firulais"]
}
for key, value in persona.items():
    print(key, value)