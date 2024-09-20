'''
Codigo para dictaminar el precio de cada mango
segun la oferta de 3x2
'''


def mango(cantidad, precio_por_mango):
    # Calcula el número de mangos que se pagan (por cada 3 mangos, solo se pagan 2)
    mangos_pagados = cantidad - (cantidad // 3)

    # Calcula el costo total
    costo_total = mangos_pagados * precio_por_mango

    return costo_total


# Ejemplos de uso
print(mango(2, 3))  # Salida: 6
print(mango(3, 3))  # Salida: 6
print(mango(5, 3))  # Salida: 12
print(mango(9, 5))  # Salida: 30
