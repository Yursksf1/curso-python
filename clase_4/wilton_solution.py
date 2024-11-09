# 2) define una tupla con los dias de la semana en minuscula empezando por lunes 
#     - iprimie el tercer dia en mayuscula
#     - iprimie el ultimo dia con la primera letra en mayuscula

print("EJERCICIO 2")
dias=("lunes","martes","miercoles","jueves","viernes","sabado","domingo")

print("iprimie el tercer dia en mayuscula")
print(dias[2].upper())
print("#     - iprimie el ultimo dia con la primera letra en mayuscula")
dultimo=len(dias)
print(dias[dultimo-1].capitalize())

# -----------------------
dias_semana= ("lunes", "martes", "miercoles","jueves", "viernes", "sabado", "domingo")
print(dias_semana)
print(dias_semana[2].upper())
print(dias_semana[6].capitalize())

# --------------------------

dias = ( "lunes", "martes","miercoles","jueves","viernes","sabado","domingo")
print('dias semana:',dias)
dias_mayuscula=list(map(str.upper, dias))
dias_titulo=list(map(str.title, dias))
print('dias semana:',dias_mayuscula)
print('dias semana:',dias[3].upper())
longitud=len(dias)
print ('numero dias semana:',longitud)
print('dias semana:',dias_titulo[longitud-1])