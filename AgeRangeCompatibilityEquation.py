'''
Programa para tener un minimo y maximo ideal
de la edad para salir con alguien
'''

def dating_range(age):
    if age > 14:
        min_age = age // 2 + 7
        max_age = (age - 7) * 2
    else:
        min_age = int(age - 0.10 * age)
        max_age = int(age + 0.10 * age)

    return f"{min_age}-{max_age}"


# Ejemplos de uso
print(dating_range(27))  # Salida: "20-40"
print(dating_range(20))  # Salida: "17-26"
print(dating_range(17))  # Salida: "15-20"
