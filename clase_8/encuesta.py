import time

def medir_tiempo(funcion):
    def wrapper(*args, ** kwargs):
        inicio = time.time() # Momento en que se inicia la ejecución de la función
        resultado = funcion(*args, ** kwargs) # Llamada a la funcion original
        fin = time.time() # Momento en que se finaliza la ejecución de la función
        tiempo_transcurrido = fin - inicio
        return resultado, tiempo_transcurrido
    return wrapper

@medir_tiempo
def contesta_pregunta(pregunta):
    respuesta = input(pregunta)
    return respuesta

preguntas = [
    "que opina del alcalde de bucaramanga? ",
    "cual es la mejor gestion que considera que se ha desarrollado en el gov? ",
    "cual es la calle mas transitada en la ciudad? ",
]

respuestas = []
tiempos = []
for idx, pregunta in enumerate(preguntas):
    respuesta = contesta_pregunta(f"{idx+1}. {pregunta}")
    respuestas.append(respuesta[0])
    tiempos.append(respuesta[1])

print('### RESPUESTAS ###')
# imprimiendo las preguntas con sus respuestas
for i in range(len(preguntas)):
    print(preguntas[i])    
    print(respuestas[i])    
    print(tiempos[i])
    print("")