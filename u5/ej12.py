numeros = []

for i in range(8):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

print(f"Lista original: {numeros}")

numeros_menor_mayor = sorted(numeros)
print(f"Ordenada de menor a mayor: {numeros_menor_mayor}")

numeros_mayor_menor = sorted(numeros, reverse=True)
print(f"Ordenada de mayor a menor: {numeros_mayor_menor}")