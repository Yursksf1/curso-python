contador = 0
while True:
    contador = contador +1
    print('contador con valor de: ', contador)
    if contador > 100:
        break
    
contador = 0
condicion = True
while condicion:
    contador = contador +1
    print('contador con valor de: ', contador)
    salir_programa = input('Desea salir del programa? (S/N)') == "S"
    
    if salir_programa:
        condicion = False

print('he salido del ciclo while')