notas = [3, 6, 7, 4, 6, 9, 10, 2, 5, 8]

print("--- Lista de Notas ---")
for i in range(len(notas)):
    print(f"Estudiante {i + 1}: {notas[i]}")

# Variables inicializadas con el primer elemento de la lista
suma_notas = 0
nota_alta = notas[0]
nota_baja = notas[0]

# Recorrido para acumulacion y comparacion
for nota in notas:
    suma_notas += nota
    if nota > nota_alta:
        nota_alta = nota
    if nota < nota_baja:
        nota_baja = nota

promedio = suma_notas / len(notas)

# Mostrar resultados finales
print("\n--- Resultados ---")
print(f"Promedio: {promedio}")
print(f"Nota más alta: {nota_alta}")
print(f"Nota más baja: {nota_baja}")