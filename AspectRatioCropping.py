def aspect_ratio_16_9(x, y):
    # Calcula el nuevo ancho para que la imagen tenga una relación de aspecto de 16:9
    new_x = round((16 / 9) * y)
    # Devuelve el nuevo tamaño de la imagen con la misma altura
    return new_x, y

# Ejemplo de uso con dimensiones 374 x 280
resultado = aspect_ratio_16_9(374, 280)
print(f"Nuevo tamaño con relación 16:9: {resultado[0]} x {resultado[1]}")