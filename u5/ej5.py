estudiantes_presentes = ["Octavio", "Leo", "Joaquin", "Lisandro", "Guillermo", "Alan", "Martin", "Jorge"]

print("--- Lista de estudiantes presentes ---")
for index in range(len(estudiantes_presentes)):
    print(f"{index + 1}. {estudiantes_presentes[index]}")

print("--------------------------------------")
print("1. Eliminar estudiante")
print("2. Añadir estudiante")
decision_usuario = int(input("Ingrese el número de la acción que desea realizar: "))

if decision_usuario == 1:
    estudiante_a_eliminar = int(input("Elige el número del estudiante a eliminar: "))
    del estudiantes_presentes[estudiante_a_eliminar - 1]
elif decision_usuario == 2:
    estudiante_a_anadir = input("Escribe el nombre del estudiante a añadir: ")
    estudiantes_presentes.append(estudiante_a_anadir)

print("--- Lista de estudiantes presentes ---")
for index in range(len(estudiantes_presentes)):
    print(f"{index + 1}. {estudiantes_presentes[index]}")