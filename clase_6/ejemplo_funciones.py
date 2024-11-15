def saludar():
    print('Hola mundo, feliz dia ')

saludar()
saludar()
saludar()
saludar()
saludar()

def get_saludo():
    return 'Hola a todos, feliz dia '


saludo = saludar()
print(saludo)


saludo = get_saludo()
saludo = get_saludo()
saludo = get_saludo()
saludo = get_saludo()
saludo = get_saludo()
print(saludo)


def saluda_me(nombre):
    print(f"Hola {nombre}, Feliz dia")


saluda_me('Yurley')
saluda_me('Camila')
saluda_me('Sebastian')
saluda_me('Jorge')


def get_saluda_me(nombre):
    return f"Hola {nombre}, Hoy es un bonito dia"


saludo = get_saluda_me('Yurley')
saludo = get_saluda_me('Camila')
saludo = get_saluda_me('Sebastian')
saludo = get_saluda_me('Jorge')
print(saludo)



# EJEMPLO:
"""
definir una funcion Conversor de COP a dolares (valor del dolar: 1 USD = 4.473 COP)
"""

def usd_to_cop(money_usd):
    valor = money_usd * 4473
    return valor

def cop_to_usd(money_cop):
    valor = money_cop / 4473
    return valor

valor_en_pesos = usd_to_cop(50)
print(valor_en_pesos, "COP")


valor_en_pesos = cop_to_usd(500000)
print(valor_en_pesos, "USD")