
def limpar_data(funcion):
    def wrapper(*args, ** kwargs):
        resultado = funcion(*args, ** kwargs) # Llamada a la funcion original

        resultado = resultado.strip()
        resultado = resultado.upper()
        return resultado
    return wrapper

@limpar_data
def get_nombre():
    nombre = input("Ingresa el tu nombre: ")
    return nombre

@limpar_data
def get_apellido():
    nombre = input("Ingresa el tu apellido: ")
    return nombre

def get_ciudad():
    nombre = input("Ingresa el tu ciudad: ")
    return nombre



nombre = get_nombre()
apellido = get_apellido()
ciudad = get_ciudad()

print(f"hola {nombre} {apellido} hoy es un bonito dia en la ciudad de {ciudad}")
