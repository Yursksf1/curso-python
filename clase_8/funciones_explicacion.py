def saludar(nombre, apellido=""):
    print(f"hola {nombre} {apellido}")

def saludar_v2(*args, **kwargs):
    print(f"hola {args}, {kwargs}")


saludar_v2("Yurley")
saludar_v2("Yurley", "Sanchez")
saludar_v2(nombre="Yurley", apellido="Sanchez")