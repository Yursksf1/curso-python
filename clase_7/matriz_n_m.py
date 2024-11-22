import random 

lista =  [1,2,3,4]
lista_1 =  [0,0,0,0]
lista_2 =  [0,0,0,0]

matriz = [
    lista,
    lista_1,
    lista_2
]

print(matriz)

for vector in matriz:
    print(vector)
print('----------------')

# dinamica
# caracter = input('ingresa el caracter de la matriz: ')
# n_filas = int(input('ingresa el numero de filas: '))
# n_columnas = int(input('ingresa numero de columnas: '))
#
# new_matriz = [[caracter for _ in range(n_filas)] for _ in range(n_filas)]

# for vector in new_matriz:
#     print(vector)

# matriz identidad:
n_filas = int(input('ingresa la dimencion de la matriz n*n: '))
# new_matriz = [[0]*n_filas]*n_filas
new_matriz = [[0 for _ in range(n_filas)] for _ in range(n_filas)]

contador_i = 0
contador_j = 0

for vector in new_matriz:
    print(vector)
print('')

for vector in new_matriz:
    for elemento in vector:
        if contador_i == contador_j:
            new_matriz[contador_i][contador_j] = 1
        contador_j = contador_j + 1
    contador_j = 0
    contador_i = contador_i + 1

for vector in new_matriz:
    print(vector)
print('')

new_matriz = [[random.randint(0,9) for _ in range(n_filas)] for _ in range(n_filas)]
for vector in new_matriz:
    print(vector)