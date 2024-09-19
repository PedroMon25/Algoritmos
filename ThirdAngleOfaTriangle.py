'''
Programa para obtener el 3er angulo de un triangulo con 2 valores
'''


def tercer_angulo(angulo1, angulo2):
    # Calcula el tercer ángulo
    return 180 - (angulo1 + angulo2)

# Ejemplo de uso
angulo1 = 42
angulo2 = 30
print(tercer_angulo(angulo1, angulo2))  # Salida: 50
