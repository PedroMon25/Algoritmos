def nba_extrap(ppg, mpg):
    # Si los minutos por partido son 0, devolver 0 para evitar división por cero
    if mpg == 0:
        return 0

    # Calcular la extrapolación de puntos a 48 minutos y redondear a la décima más cercana
    extrapolated_ppg = (ppg / mpg) * 48
    return round(extrapolated_ppg, 1)


# Ejemplos de uso
print(nba_extrap(12, 20))  # Salida: 28.8
print(nba_extrap(10, 10))  # Salida: 48
print(nba_extrap(5, 17))  # Salida: 14.1
print(nba_extrap(0, 0))  # Salida: 0
