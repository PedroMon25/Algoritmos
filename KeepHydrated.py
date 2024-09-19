import math

def litros_de_agua(tiempo_horas):
    # Calcula la cantidad de litros y redondea hacia abajo
    return math.floor(tiempo_horas * 0.5)

# Ejemplo de uso
tiempo_horas = 6
print(litros_de_agua(tiempo_horas))  # Salida: 1
