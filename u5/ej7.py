temperaturas = [
    [10, 22],
    [12, 25],
    [8, 20],
    [15, 28],
    [11, 24],
    [9, 19],
    [13, 26]
]

minimas = []
maximas = []
amplitud_termica = temperaturas[0]
dia_mayor_amplitud = 0

for index in range(len(temperaturas)):
    temperatura = temperaturas[index]

    minimas.append(temperatura[0])
    maximas.append(temperatura[1])

    if temperatura[1] - temperatura[0] > amplitud_termica[1] - amplitud_termica[0]:
        amplitud_termica = temperatura
        dia_mayor_amplitud = index + 1

suma_minimas = sum(minimas)
suma_maximas = sum(maximas)

promedio_minimas = int(suma_minimas / len(temperaturas))
promedio_maximas = int(suma_maximas / len(temperaturas))

print("------- Los últimos 7 días -------")
print(f"Promedio de temperaturas mínimas: {promedio_minimas}")
print(f"Promedio de temperaturas máximas: {promedio_maximas}")
print(f"El día {dia_mayor_amplitud} fue el día de mayor amplitud térmica con {amplitud_termica[1] - amplitud_termica[0]} grados de diferencia entre mínima y máxima")