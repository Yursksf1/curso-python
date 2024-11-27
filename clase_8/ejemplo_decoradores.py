
## caso de errores
def division(a, b):
    try:
        return a / b
    except:
        return "hubo un error"

def sumar(a, b):
    try:
        return a + b
    except:
        return "hubo un error"

def restar(a, b):
    try:
        return a - b
    except:
        return "hubo un error"

#resultado = division(1, 0)
resultado = restar(1, "w")
print(resultado)