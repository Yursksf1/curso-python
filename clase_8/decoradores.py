import time

def operacion_costosa(n):
    # Simulamos una operación costosa con un bucle
    suma = 0
    for i in range(n):
        suma += i
    return suma

def operacion_costosa_n2(n):
    # Simulamos una operación costosa con un bucle
    suma = 0
    for i in range(n):
        for j in range(n):
            suma += i + j
    return suma

# Ejemplo de uso
print("empieza")
inicio = time.time()
resultado = operacion_costosa(10000)
fin = time.time()
tiempo_transcurrido = fin - inicio
print('la funcion dardo: ', tiempo_transcurrido)

print("El resultado de la operación costosa es:", resultado)
print("termina")


print("empieza")
inicio = time.time()
resultado = operacion_costosa_n2(10000)
fin = time.time()
tiempo_transcurrido = fin - inicio
print('la funcion dardo: ', tiempo_transcurrido)

print("El resultado de la operación costosa es:", resultado)
print("termina")
