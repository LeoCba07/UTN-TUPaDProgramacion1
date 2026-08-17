estudiantes = [
    "Octavio",
    "Leo",
    "Joaquin",
    "Lisandro",
    "Guillermo",
    "Alan",
    "Martin",
    "Jorge",
    "Nicolas",
    "Emiliano"
]

nombre_buscar = input("Ingrese el nombre del estudiante a buscar: ")

if nombre_buscar in estudiantes:
    posicion = estudiantes.index(nombre_buscar)

    print(f"El estudiante {nombre_buscar} se encuentra en la lista.")
    print(f"Su posición es: {posicion + 1}")
else:
    print(f"El estudiante {nombre_buscar} no se encuentra en la lista.")