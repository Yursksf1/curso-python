# generador de secuencia fibonnaci hasta el numero n
#ejemplo: 1 1 2 3 5 8 13 21 34 55


def get_fibonnaci(numero):
    anterior = 0
    nuevo = 1
    resultado = None

    contador = 1
    lista_f = []
    while contador <= numero:
        resultado = anterior + nuevo
        print (f"{contador}. {anterior} + {nuevo} = {resultado}" )
        contador = contador + 1
        anterior = nuevo
        nuevo = resultado
        lista_f.append(nuevo)
    
    return lista_f



numero = int(input("Ingresa el numero: "))
print(numero)
lista_f = get_fibonnaci(numero)
print('lista f', lista_f)



numero = int(input("Ingresa el numero: "))
print(numero)
lista_f = get_fibonnaci(numero)
print('lista f', lista_f)