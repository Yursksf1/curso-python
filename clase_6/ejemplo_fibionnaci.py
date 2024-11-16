# generador de secuencia fibonnaci hasta el numero n
#ejemplo: 1 1 2 3 5 8 13 21 34 55


numero = int(input("Ingresa el numero: "))
print(numero)

anterior = 0
nuevo = 1
resultado = None

contador = 1
lista_f = []
while contador < numero:
    contador = contador + 1
    resultado = anterior + nuevo
    print (f"{contador}. {anterior} + {nuevo} = {resultado}" )

    anterior = nuevo
    nuevo = resultado
    lista_f.append(nuevo)

print(lista_f)