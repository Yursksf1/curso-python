# #Ejercicio 1
# Nombre = input('Ingrese su nombre= ')
# print(f'Nombre que ingreso:{Nombre}'.lower())
# print(f'Nombre Mayuscula:{Nombre}'.upper())
# print(f'Nombre primeras letras mayuscula:{Nombre}'.title())


# #Ejercicio 2
# Nombre_Familiar= input('Ingrese Nombre de familiar= ')
# print(f'Nombre que ingreso:{Nombre_Familiar.upper()}')
# print(f'Nombre primera letra mayuscula:{Nombre_Familiar.capitalize()}')
# print(f'Nombre Letra de cada palabra mayuscula:{Nombre_Familiar.title()}')

#Ejercicio 3
texto = input('Ingrese Texto= ')
texto = texto.lower()
param = [('a','4'),('e','3'),('i','1'),('o','0')]
for key, value in param:
    texto = texto.replace(key, value)
    
# texto = texto.replace(
# 'A', '4').replace('E', '3').replace('I', '1').replace('O', '0')
print(texto)