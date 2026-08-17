datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datos_no_repetidos = []

# Iteramos sobre los datos -> si no están en la nueva lista, los insertamos.
for dato in datos:
    if dato not in datos_no_repetidos:
        datos_no_repetidos.append(dato)

print(datos)
print(datos_no_repetidos)