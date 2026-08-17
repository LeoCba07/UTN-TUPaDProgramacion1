products = []

for i in range(5):
    product = input(f"Ingresa el nombre del producto {i + 1}: ")
    products.append(product)

# Organizamos alfabeticamente y reemplazamos los valores de la lista
products = sorted(products, key=str.lower)

for index in range(len(products)):
    print(f"{index + 1}. {products[index]}")

product_to_delete = int(input("Ingrese el número del producto que desea eliminar: "))

# Eliminamos el elemento de la lista basados en su indice menos 1
del products[product_to_delete - 1]

for index in range(len(products)):
    print(f"{index + 1}. {products[index]}")