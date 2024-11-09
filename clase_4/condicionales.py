edad = int(input("ingresa tu edad: "))
if edad >= 18:
    print('eres mayor de edad')
else:
    print('eres menor de edad')


# clasificador de edad
if edad < 1:
    print("Eres un bebé. ")
elif edad < 13:
    print("Eres un niño. ")
elif edad < 18:
    print("Eres un adolescente. ")
elif edad < 30:
    print("Eres un adulto joven.")
elif edad < 60:
    print("Eres un adulto. ")
elif edad < 80:
    print("Eres un adulto mayor. ")
else:
    print("Eres una persona de edad avanzada. ")

es_mujer = input('Eres una mujer? S/N: ') == "S"

if edad>18 and es_mujer:
    print("Tienes un credito pre-aprobado en el banco de la mujer")
if edad>18 and not es_mujer:
    print("Tienes un la posibilidad de sacar otro tipo de credito")
