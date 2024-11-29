import time

def medir_tiempo(funcion):
    def wrapper(*args, ** kwargs):
        inicio = time.time() # Momento en que se inicia la ejecución de la función
        resultado = funcion(*args, ** kwargs) # Llamada a la funcion original
        fin = time.time() # Momento en que se finaliza la ejecución de la función
        tiempo_transcurrido = fin - inicio
        print(f"La función {funcion.__name__} tardó {tiempo_transcurrido} segundos en ejecutarse.")
        return resultado, tiempo_transcurrido
    return wrapper

@medir_tiempo
def operacion_costosa(n):
    # Simulamos una operación costosa con un bucle
    suma = 0
    for i in range(n):
        suma += i
    return suma

@medir_tiempo
def operacion_costosa_n2(n):
    # Simulamos una operación costosa con un bucle
    suma = 0
    for i in range(n):
        for j in range(n):
            suma += i + j
    return suma

# Ejemplo de uso
print("empieza")
resultado = operacion_costosa(10000)
print("El resultado de la operación costosa es:", resultado)
print("termina")


print("empieza")
resultado = operacion_costosa_n2(10000)
print("El resultado de la operación costosa es:", resultado)
print("termina")
