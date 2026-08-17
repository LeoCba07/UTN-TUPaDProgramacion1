puntajes = [450, 1200, 875, 990, 300, 1500, 640]

puntaje_mas_alto = max(puntajes)
puntaje_mas_bajo = min(puntajes)

ranking = sorted(puntajes, reverse=True)

posicion_990 = ranking.index(990) + 1

print(f"Puntaje más alto: {puntaje_mas_alto}")
print(f"Puntaje más bajo: {puntaje_mas_bajo}")
print(f"Ranking: {ranking}")
print(f"El puntaje 990 se encuentra en la posición {posicion_990} del ranking.")