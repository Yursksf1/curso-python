"""
3) define una estructura para almacenar el himno nacional, que este por estrofas
    ejemplo: 
    {
        "estrofa 1": '''Cesó la horrible noche 
                        La libertad sublime 
                        Derrama las auroras 
                        De su invencible luz. 
                        La humanidad entera, 
                        Que entre cadenas gime, 
                        Comprende las palabras 
                        Del que murió en la cruz ''',
        "estrofa 2": '''"Independencia" grita 
                        El mundo americano: 
                        Se baña en sangre de héroes 
                        La tierra de Colón. 
                        Pero este gran principio: "el rey no es soberano" 
                        Resuena, Y los que sufren 
                        Bendicen su pasión.  ''',

    }
    - imprimir la estrofa numero 10, 
    - imprimir el numero de estrofas, 
"""

himno = {
    "Primera estrofa": """
        Cesó la horrible noche 
        La libertad sublime 
        Derrama las auroras 
        De su invencible luz. 
        La humanidad entera, 
        Que entre cadenas gime, 
        Comprende las palabras 
        Del que murió en la cruz
    """,
    "Segunda estrofa": """
        "Independencia" grita 
        El mundo americano: 
        Se baña en sangre de héroes 
        La tierra de Colón. 
        Pero este gran principio: "el rey no es soberano" 
        Resuena, Y los que sufren 
        Bendicen su pasión. 
    """,
    "Tercera estrofa": """
        Del Orinoco el cauce 
        Se colma de despojos, 
        De sangre y llanto un río Se mira allí correr. 
        En Bárbula no saben 
        Las almas ni los ojos 
        Si admiración o espanto 
        Sentir o padecer. 
    """,
    "Cuarta estrofa": """
        A orillas del Caribe 
        Hambriento un pueblo lucha Horrores prefiriendo 
        A pérfida salud. 
        Oh, sí de Cartagena 
        La abnegación es mucha, 
        Y escombros de la muerte 
        desprecian su virtud.
    """,
    "Quinta estrofa": """
        De Boyacá en los campos 
        El genio de la gloria 
        Con cada espiga un héroe 
        invicto coronó. 
        Soldados sin coraza 
        Ganaron la victoria; 
        Su varonil aliento 
        De escudo les sirvió.
    """,
    "Sexta estrofa": """
        Bolívar cruza el Ande 
        Que riega dos océanos 
        Espadas cual centellas 
        Fulguran en Junín. 
        Centauros indomables 
        Descienden a los llanos 
        Y empieza a presentirse 
        De la epopeya el fin.
    """,
    "Séptima estrofa": """
        La trompa victoriosa 
        Que en Ayacucho truena 
        En cada triunfo crece 
        Su formidable són. 
        En su expansivo empuje 
        La libertad se estrena, 
        Del cielo Americano 
        Formando un pabellón. 
    """,
    "Octava estrofa": """
        La Virgen sus cabellos 
        Arranca en agonía 
        Y de su amor viuda 
        Los cuelga del ciprés. 
        Lamenta su esperanza 
        Que cubre losa fría; 
        Pero glorioso orgullo 
        circunda su alba tez. 
    """,
    "Novena estrofa": """
        La Patria así se forma 
        Termópilas brotando; 
        Constelación de cíclopes Su noche iluminó; 
        La flor estremecida 
        Mortal el viento hallando 
        Debajo los laureles
        Seguridad buscó 
    """,
    "Décima estrofa": """
        Mas no es completa gloria Vencer en la batalla, 
        Que al brazo que combate Lo anima la verdad. 
        La independencia sola 
        El gran clamor no acalla: 
        Si el sol alumbra a todos 
        Justicia es libertad.
    """,
    "Undécima estrofa": """
        Del hombre los derechos 
        Nariño predicando, 
        El alma de la lucha 
        Profético enseñó. 
        Ricaurte en San Mateo 
        En átomos volando 
        "Deber antes que vida", 
        Con llamas escribió. 
    """,
}

print(himno.get('Décima estrofa'))
print(himno['Décima estrofa'])
print(himno.keys())

print(len(himno.keys()))

contador_lineas = 0
for estrofa in himno.keys():
    print(estrofa)
    print(himno.get(estrofa))
    valor_estrofa = himno.get(estrofa)
    lineas = valor_estrofa.split('\n')
    lineas_en_estrofa = len(lineas)
    contador_lineas = contador_lineas + lineas_en_estrofa

print('el himno tiene esta cantidad de linesa: ', contador_lineas)
