"""
    2. Crear una aplicación Para un centro deportivo (GIMNASIO) que cuenta con las siguientes características
- Bronce Plata Oro, dicha clasificación es determinada por el número de horas que realiza en el mes.

Nombre
Bronce
Plata
Oro
Número de Horas x Mes
(0 -- 15]
(15 -- 30]
(30 --
Valor por hora
5.000
3.500
2.000


Hacer un programa en Python 
Para la gestión del centro deportivo.
- La facturación del servicio y descuento aplicado

Ejemplo

    • Juan estuvo en el gimnasio 25 horas en el mes, por lo tanto se le aplica factura de suscripción plata, por un valor de 3500 / hora por lo tanto 
25 * 3.500 = 87.500

    • Mary estuvo en el gimnasio 10 horas en el mes, por lo tanto se le aplica factura de suscripción bronce, por un valor de 5000 / hora por lo tanto 
10 * 5000 = 50.000

    • Daniel estuvo en el gimnasio 35 horas en el mes
        ◦ cuanto se le deberia cobrar?
"""
clasificacion={
    "bronce": 5000,
    "plata": 3500,
    "oro": 2000
}

clientes={"codigo":[],"nombre":[],"horasconsumidas":[]}

facturacion={"codigo":[],"nombre":[],"horasconsumidas":[],"categoria":[],"valorhora":[],"total":[]}

numeroclientes=int(input("Digite el numero de Clientes ha facturar="))

i=0
while i<numeroclientes:
    codigo=i+1
    nombre=input("digite nombre cliente=")
    horas=int(input("horas consumidas="))
    clientes["codigo"].append(codigo)
    clientes["nombre"].append(nombre)
    clientes["horasconsumidas"].append(horas)	
    i=i+1


print("{:<{}} {:<{}} {:<{}} {:<{}} {:<{}}".format("COIDGO", 3, "NOMBRE", 20, "HORAS CONSUMIDAS", 5, "CATEGORIA", 8, "TOTAL FACTURA", 8))

i=0
while i<numeroclientes:
    codigo=clientes.get("codigo")
    codigo=codigo[i]
    nombre=clientes.get("nombre")
    nombre=nombre[i]
    horas=clientes.get("horasconsumidas")
    horas=horas[i]
    categoria = ""
    if horas<=15:
        categoria="bronce"  
    elif horas<=30: 
        categoria="plata"
    else: 
        categoria="oro"

    total =  horas * clasificacion.get(categoria, 0)
    facturacion["codigo"].append(codigo)
    facturacion["nombre"].append(nombre)
    facturacion["horasconsumidas"].append(horas) 
    facturacion["categoria"].append(categoria)   
    facturacion["valorhora"].append(3500)
    facturacion["total"].append(total)  

    print("{:<{}} {:<{}} {:<{}} {:<{}} {:<{}}".format(codigo, 3, nombre, 20, horas, 5, categoria, 8, total, 8))

    
    i=i+1
