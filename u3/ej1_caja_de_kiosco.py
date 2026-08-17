client_name = input("Ingrese su nombre: ")

# Validar que no quede vacio y sean solo letras
while client_name == "" or not client_name.isalpha():
    client_name = input("Solo letras, ingrese su nombre nuevamente: ")

product_quantity = input("Ingrese la cantidad de productos a comprar: ")

# Validar entero positivo mayor a cero
while not product_quantity.isdigit() or int(product_quantity) == 0:
    product_quantity = input("No es válido, ingrese la cantidad de productos nuevamente: ")

product_quantity = int(product_quantity)

regular_total = 0
final_total = 0.0

for i in range(product_quantity):

    price = input(f"Ingrese el precio del producto {i + 1}: ")

    while not price.isdigit():
        price = input("Sólo numeros enteros, ingrese el precio nuevamente: ")

    price = int(price)

    discount = input("¿Tiene descuento? (S/N): ").upper()

    # Validar que ingrese solo S o N
    while discount not in ["S", "N"]:
        discount = input("Opción inválida. ¿Tiene descuento? (S/N): ").upper()

    # Aplicar descuento
    if discount == "S":
        discounted_price = price * 0.90
        final_total += discounted_price
    else:
        final_total += price

    regular_total += price


# Cálculos de los totales y promedio
saved_total = regular_total - final_total
average_price = final_total / product_quantity

# Mostrar los resultados formateados
print(f"Cliente: {client_name}")
print(f"Cantidad de productos: {product_quantity}")
print(f"Total sin descuentos: ${regular_total}")
print(f"Total con descuentos: ${final_total:.2f}")
print(f"Ahorro: ${saved_total:.2f}")
print(f"Promedio por producto: ${average_price:.2f}")
