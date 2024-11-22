def palabras_no_repetidas(cancion):
    letra = cancion.lower().replace(",", "").replace("!", "")
    palabras = letra.split()

    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

micancion={
"pollito_pio":"""
En la radio, hay un pollito
En la radio, hay un pollito
El pollito popo, el pollito pío
El pollito pío, el pollito pío
El pollito pío, el pollito pío

En la radio, hay una gallina
En la radio, hay una gallina
Y la gallina coo, y el pollito pío
Y el pollito pío, y el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay también un gallo
En la radio, hay también un gallo
Y el gallo corococo, y la gallina coo
Y el pollito pío, el pollito pío
El pollito pío, el pollito pío

En la radio, hay un pavo
En la radio, hay un pavo
Y el pavo glugluglu, y el gallo corococo
Y la gallina coo, y el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay una paloma
En la radio, hay una paloma
Y la paloma ruuu, el pavo glugluglu
El gallo corococo, y la gallina coo
El pollito pío, el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay también un gato
En la radio, hay también un gato
Y el gato miao, la paloma ruuu
El pavo glugluglu, el gallo corococo
Y la gallina coo, y el pollito pío
El pollito pío, y el pollito pío

En la radio, hay también un perro
En la radio, hay también un perro
Y el perro guau guau, el gato miao
La paloma ruu, el pavo glugluglu
El gallo cocoroco, y la gallina coo
Y el pollito pío, y el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay una cabra
En la radio, hay una cabra
Y la cabra mee, el perro guau guau
El gato miao, y la paloma ruu
El pavo glugluglu, el gallo cocoroco
Y la gallina coo, y el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay un cordero
En la radio, hay un cordero
Y el cordero bee, y la cabra mee
El perro guau guau, el gato miao
La paloma ruu, el pavo glugluglu
El gallo cocoroco, y la gallina coo
Y el pollito pío, y el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay una vaca
En la radio, hay una vaca
Y la vaca moo, y el cordero bee
Y la cabra mee, el perro guau guau
El gato miao, y la paloma ruu
El pavo glugluglu, el gallo cocoroco
Y la gallina coo, y el pollito pío
Y el pollito pío, y el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay también un toro
En la radio, hay también un toro
Y el toro muu, y la vaca moo
Y el cordero bee, y la cabra mee
El perro guau guau, el gato miao
La paloma ruu, el pavo glugluglu
El gallo cocoroco, y la gallina coo
Y el pollito pío, y el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay un tractor
En la radio, hay un tractor
Y el tractor brum, y el tractor brum
Y el tractor brum y el pollito oh-oh
""",
"baby shark":"""
Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark!

Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark!

Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark!

Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark!

Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark!

Let’s go hunt, doo doo doo doo doo doo
Let’s go hunt, doo doo doo doo doo doo
Let’s go hunt, doo doo doo doo doo doo
Let’s go hunt!

Run away, doo doo doo doo doo doo
Run away, doo doo doo doo doo doo
Run away, doo doo doo doo doo doo
Run away!

Safe at last, doo doo doo doo doo doo
Safe at last, doo doo doo doo doo doo
Safe at last, doo doo doo doo doo doo
Safe at last!

It’s the end, doo doo doo doo doo doo
It’s the end, doo doo doo doo doo doo
It’s the end, doo doo doo doo doo doo
It’s the end!

"""
}

contador_palabas = palabras_no_repetidas(micancion.get("pollito_pio"))
for key, value in contador_palabas.items():
    print(key, value)

print('------')
contador = 0
for key, value in contador_palabas.items():
    if value < 5:
        contador = contador +1 
        print(key, value)

print('cantidad total de palabras: ', sum(contador_palabas.values()))
print('cantidad de palabras no repetidas: ', len(contador_palabas.keys()))
print('la cantidad de palabras que se repitern menos de 5 veces es: ', contador)