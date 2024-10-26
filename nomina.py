nombre = 'Juan'
valor_por_hora = 20000
horas_trabajadas = 200
resultado = valor_por_hora*horas_trabajadas

def calcular_salario(
        valor_por_hora, 
        horas_trabajadas, 
        horas_extras, 
        horas_extras_nocturnas, 
        horas_extras_dominicales
    ):
    pago_general = valor_por_hora * horas_trabajadas
    pago_horas_extras = horas_extras * valor_por_hora * 1.25
    pago_horas_extras_n = horas_extras_nocturnas * valor_por_hora * 1.35
    pago_horas_extras_d = horas_extras_dominicales * valor_por_hora * 2.13

    total_devengado = pago_general + pago_horas_extras + pago_horas_extras_n + pago_horas_extras_d

    if total_devengado < 2000000:
        # agrega aux de transporte
        total_devengado = total_devengado + 140000
    elif total_devengado > 4000000:
        # aplica retencion en la fuente, se retiene el 1% para impuestos
        total_devengado = total_devengado * 0.9
    
    # para restar salud y pension
    pagos_salud_pension = total_devengado * 0.08
    total_devengado = total_devengado - pagos_salud_pension

    return total_devengado


"""
1) si el empleado gana menos de 2 salarios minimos (2 millones aprox) entonces
    tiene derecho al aux de transporte: 140.000
2) si el empleado gana 4 salarios minimos se debe aplicar retencion en la fuente, 1% 
3) todo empleado debe hacer aporte a salud y pension correspondiente al 8% de su salario 
4) algunos empleado tienen horas extras que son pagadas 1.25 %
5) las horas nocturnas se pagan con un aumento del 1.35% 
6) las horas trabajadas los dominicales sepagan 2.13%
"""



print(f"""
    el empleado {nombre}, 
    trabajo: {horas_trabajadas} de horas, y 
    su valor por hora es de {valor_por_hora} 
    por lo tanto debemos pagarle {resultado} """)


"""
valor_por_hora, 
horas_trabajadas, 
horas_extras, 
horas_extras_nocturnas, 
horas_extras_dominicales
"""

salario = calcular_salario(
    9800,
    120,
    40,
    15,
    0
)
print('el salario calculado es: ', salario)