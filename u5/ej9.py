tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

print("--- Jugador X ---")
fila = int(input("Ingrese la fila (1-3): "))
columna = int(input("Ingrese la columna (1-3): "))

tablero[fila - 1][columna - 1] = "X"

for fila in tablero:
    print(fila)


print("--- Jugador O ---")
fila = int(input("Ingrese la fila (1-3): "))
columna = int(input("Ingrese la columna (1-3): "))

tablero[fila - 1][columna - 1] = "O"

for fila in tablero:
    print(fila)