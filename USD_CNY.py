'''
Codigo para convertir un valor monetario de dolar estadounidense a yuan chino
'''


def convertir_usd_a_cny(usd):
    tasa_conversion = 7.1  # Tasa de conversión de USD a CNY
    cny = usd * tasa_conversion
    return f"{cny:.2f} yuanes chinos"

# Ejemplo de uso
usd = 777  # Monto en dólares estadounidenses
resultado = convertir_usd_a_cny(usd)
print(resultado)
