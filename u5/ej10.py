ventas = [
    [10, 15, 12, 20, 18, 14, 16],  # Producto 1
    [8, 12, 10, 15, 20, 18, 14],    # Producto 2
    [20, 18, 15, 22, 25, 20, 24],   # Producto 3
    [5, 10, 8, 12, 15, 10, 9]       # Producto 4
]

totales_productos = []

# Total vendido por cada producto
for producto in ventas:
    total = sum(producto)
    totales_productos.append(total)

for index in range(len(totales_productos)):
    print(f"Total vendido del producto {index + 1}: {totales_productos[index]}")

# Día con mayores ventas totales
mayor_venta = 0
dia_mayor_venta = 0

for dia in range(7):
    total_dia = 0

    for producto in ventas:
        total_dia += producto[dia]

    if total_dia > mayor_venta:
        mayor_venta = total_dia
        dia_mayor_venta = dia + 1

print(f"El día con mayores ventas fue el día {dia_mayor_venta}, con {mayor_venta} ventas")

# Producto más vendido en la semana
mayor_producto = max(totales_productos)
producto_mas_vendido = totales_productos.index(mayor_producto) + 1

print(f"El producto más vendido fue el producto {producto_mas_vendido}, con {mayor_producto} ventas")