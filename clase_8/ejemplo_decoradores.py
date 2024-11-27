
def manejador_errores(funcion):
    def wrapper(*args, ** kwargs):
        try:
            resultado = funcion(*args, ** kwargs) # Llamada a la funcion original
        except:
            resultado = "hubo un error"
        return resultado
    return wrapper

## caso de errores
@manejador_errores
def division(a, b):
    return a / b

@manejador_errores
def sumar(a, b):
    return a + b

@manejador_errores
def restar(a, b):
    return a - b

#resultado = division(1, 0)

resultado = sumar(1, 15)
print(resultado)

resultado = sumar(1, "w")
print(resultado)