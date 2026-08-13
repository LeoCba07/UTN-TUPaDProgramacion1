# Definimos las credenciales fijas
user = "alumno"
password = "python123"

# Inicializamos la cantidad de intentos de login en 1
login_attempts = 1
login_status = False

# Secuencia de login
while login_status == False:
    user_attempt = input("Ingrese su nombre de usuario: ")
    password_attempt = input("Ingrese su contraseña: ")

    print(f"Intento {login_attempts}/3 - Usuario: {user_attempt}")
    print(f"Clave: {password_attempt}")

    if user_attempt == user and password == password_attempt:
        login_status = True
        print("Acceso concedido.")
    else:
        print("Error: credenciales inválidas.")
        login_attempts += 1

    if login_attempts == 4:
        print("Cuenta bloqueada.")
        break

# Secuencia de menú
while login_status:
    print("1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")

    # Validación de la opción
    while True:
        option = input("Elige una opción: ")
        if not option.isdigit():
            print("Error: ingrese un número válido.")
        elif int(option) not in range(1, 5):
            print("Error: opción fuera de rango.")
        else:
            option = int(option)
            break

    if option == 1:
        print("Estado: inscripto.")
    elif option == 2:
        new_password = input("Nueva clave: ")
        while len(new_password) < 6:
            print("Error: mínimo 6 caracteres.")
            new_password = input("Nueva clave: ")

        password_confirmation = input("Confirmar clave: ")

        while new_password != password_confirmation:
            print("Error: las contraseñas no coinciden.")
            new_password = input("Nueva clave: ")
            while len(new_password) < 6:
                print("Error: mínimo 6 caracteres.")
                new_password = input("Nueva clave: ")
                        
            password_confirmation = input("Confirmar clave: ")

        # Actualizamos la contraseña del sistema
        password = new_password 
        print("Clave cambiada con éxito.")
    elif option == 3:
        print("Divide cada dificultad en tantas partes como sea posible y necesario para resolverla.")
        print("-Rene Descartes")
    elif option == 4:
        print("Hasta pronto.")
        break