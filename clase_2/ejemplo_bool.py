# True y False 

# respuesta = int(input("ingresa un numero del 1 al 10: "))
# pregunta = respuesta < 5
# print("El resultado es menor que 5? ", pregunta)

'''
mayor o menor
mayor que > 
menor que <
igual == 
diferente !=

si se encuentra en una lista de elementos in 
si inicia con startwith, endwith
si es un elemento especifico  ejemplo is None
'''



respuesta = int(input("ingresa un numero del 1 al 10: ")) or None
pregunta = respuesta < 5
print("El resultado es menor que 5? ", pregunta)
pregunta = respuesta > 5
print("El resultado es mayor que 5? ", pregunta)

pregunta = respuesta == 5
print("El resultado es igual que 5? ", pregunta)

pregunta = respuesta != 5
print("El resultado es diferente que 5? ", pregunta)

lista_elementos = [0, 2, 4, 6, 8]
pregunta = respuesta in lista_elementos
print("El resultado esta en la lista de elementos ? ", pregunta)


pregunta = respuesta is None
print("El resultado es nulo ? ", pregunta)

# and / or