"""
Una empesa de telfonia movil requiere definir una estructura para
almacenar temporalmente la informacion de los usuarios

los usuarios de esta compania puede tener mas de una line movil
y cada linea movil tiene su propia facturacion

Ejemplo Base:
Juan, codigo de usuario: 123 tiene 3 lineas 
numero: 318947852 - factura: 35000
numero: 318947853 - factura: 25000
numero: 318947854 - factura: 10000
numero: 318947855 - factura: 15000


Margarita,codigo de usuario: 325  tiene 3 lineas 
numero: 317947852 - factura: 36000
numero: 317947853 - factura: 26000
numero: 317947855 - factura: 16000
....

la compania tiene mas usuarios con estas caracteristicas
"""

personas = [
    {
        "nombre": "Juan",
        "codigo": "123",
        "lineas": [
            {
                "numero":"318947852",
                "valor": 35000
            },
            {
                "numero":"318947853",
                "valor": 25000
            },
            {
                "numero":"318947854",
                "valor": 10000
            },
            {
                "numero":"318947855",
                "valor": 15000
            },
        ],
        "numero_lineas": {
            "318947852": 35000,
            "318947853": 25000,
            "318947854": 10000,
            "318947855": 15000
        }
    }, 
    {
        "nombre": "Margarita",
        "codigo": "325",
        "lineas": [
            {
                "numero":"317947852",
                "valor": 36000
            },
            {
                "numero":"317947853",
                "valor": 26000
            },
            {
                "numero":"317947855",
                "valor": 16000
            },
        ],
        "numero_lineas": {
            "317947852": 36000,
            "317947853": 26000,
            "317947855": 16000
        }
    }
]