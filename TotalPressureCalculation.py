'''
Codigo que ayuda a definir la presion segun la temperatura
'''


def presion_total(M1, M2, m1, m2, V, T_C):
    # Convertir temperatura a Kelvin
    T_K = T_C + 273.15

    # Constante de los gases ideales
    R = 0.082  # dm^3 · atm · K^-1 · mol^-1

    # Calcular la presión total usando la fórmula dada
    P_total = ((m1 / M1) + (m2 / M2)) * R * T_K / V

    return P_total


# Ejemplo de uso
M1 = 44  # Masa molar del gas 1 en g/mol
M2 = 28  # Masa molar del gas 2 en g/mol
m1 = 10  # Masa del gas 1 en gramos
m2 = 15  # Masa del gas 2 en gramos
V = 10  # Volumen del recipiente en dm^3
T_C = 25  # Temperatura en °C

print(presion_total(M1, M2, m1, m2, V, T_C))  # Salida: presión total en atm
