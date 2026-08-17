notas = [
    [8, 7, 9],
    [6, 9, 7],
    [10, 8, 9],
    [7, 6, 8],
    [9, 10, 7]
]

# Promedio de cada estudiante
for index in range(len(notas)):
    promedio = sum(notas[index]) / len(notas[index])
    print(f"Promedio del estudiante {index + 1}: {promedio}")

# Promedio de cada materia
for materia in range(3):
    suma = 0

    for estudiante in range(5):
        suma += notas[estudiante][materia]

    promedio = suma / 5

    print(f"Promedio de la materia {materia + 1}: {promedio}")