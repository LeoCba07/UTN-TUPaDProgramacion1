login_status = False

monday1 = ""
monday2 = ""
monday3 = ""
monday4 = ""

tuesday1 = ""
tuesday2 = ""
tuesday3 = ""

# Secuencia de login
while login_status == False:
    operator_name = input("Ingrese su nombre: ")

    while not operator_name.isalpha():
        print("Error: nombre inválido.")
        operator_name = input("Ingrese su nombre: ")

    login_status = True
    print(f"Bienvenido, {operator_name}")

# Secuencia de menu
while login_status == True:
    print("1. Reservar turno")
    print("2. Cancelar turno (por nombre)")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    menu_option = input("Seleccione una opción: ")

    while not menu_option.isdigit() or int(menu_option) not in range(1, 6):
        if not menu_option.isdigit():
            print("Error: no es un número.")
        else:
            print("Error: elección invalida.")
        menu_option = input("Seleccione una opción: ")

    menu_option = int(menu_option)

    # Reservar turno
    if menu_option == 1:
        print("1. Lunes")
        print("2. Martes")
        reservation_day = input("Elige un día: ")

        while not reservation_day.isdigit() or int(reservation_day) not in range(1, 3):
            if not reservation_day.isdigit():
                print("Error: no es un número.")
            else:
                print("Error: elección invalida.")
            reservation_day = input("Elige un día: ")

        reservation_day = int(reservation_day)

        # Reservar turno Lunes
        if reservation_day == 1:
            print(f"Seleccionaste: Lunes.")
            reservation_name = input("Ingresa el nombre del paciente: ")

            while not reservation_name.isalpha():
                print("Error: solo letras.")
                reservation_name = input("Ingresa nuevamente el nombre del paciente: ")

            if reservation_name == monday1 or reservation_name == monday2 or reservation_name == monday3 or reservation_name == monday4:
                print("Error: este paciente ya tiene un turno el Lunes.")
                continue

            if monday1 == "":
                monday1 = reservation_name
                print(f"Turno 1 guardado para {reservation_name} el Lunes.")
            elif monday2 == "":
                monday2 = reservation_name
                print(f"Turno 2 guardado para {reservation_name} el Lunes.")
            elif monday3 == "":
                monday3 = reservation_name
                print(f"Turno 3 guardado para {reservation_name} el Lunes.")
            elif monday4 == "":
                monday4 = reservation_name
                print(f"Turno 4 guardado para {reservation_name} el Lunes.")
            else:
                print("Todos los turnos están ocupados el Lunes")

        # Reservar turno Martes
        elif reservation_day == 2:
            print(f"Seleccionaste: Martes.")
            reservation_name = input("Ingresa el nombre del paciente: ")

            while not reservation_name.isalpha():
                print("Error: solo letras.")
                reservation_name = input("Ingresa nuevamente el nombre del paciente: ")

            if reservation_name == tuesday1 or reservation_name == tuesday2 or reservation_name == tuesday3:
                print("Error: este paciente ya tiene un turno el Martes.")
                continue

            if tuesday1 == "":
                tuesday1 = reservation_name
                print(f"Turno 1 guardado para {reservation_name} el Martes.")
            elif tuesday2 == "":
                tuesday2 = reservation_name
                print(f"Turno 2 guardado para {reservation_name} el Martes.")
            elif tuesday3 == "":
                tuesday3 = reservation_name
                print(f"Turno 3 guardado para {reservation_name} el Martes.")
            else:
                print("Todos los turnos están ocupados el Martes")

    # Cancelar turno
    elif menu_option == 2:
        print("1. Lunes")
        print("2. Martes")
        reservation_day = input("Elige un día: ")

        while not reservation_day.isdigit() or int(reservation_day) not in range(1, 3):
            if not reservation_day.isdigit():
                print("Error: no es un número.")
            else:
                print("Error: elección invalida.")
            reservation_day = input("Elige un día: ")

        reservation_day = int(reservation_day)

        # Eliminar turno Lunes
        if reservation_day == 1:
            print(f"Seleccionaste: Lunes.")
            reservation_name = input("Ingresa el nombre del paciente que quiere cancelar: ")

            while not reservation_name.isalpha():
                print("Error: solo letras.")
                reservation_name = input("Ingresa nuevamente el nombre del paciente a cancelar: ")

            if monday1 == reservation_name:
                monday1 = ""
                print(f"El Lunes Turno 1 de {reservation_name} ha sido eliminado.")
            elif monday2 == reservation_name:
                monday2 = ""
                print(f"El Lunes Turno 2 de {reservation_name} ha sido eliminado.")
            elif monday3 == reservation_name:
                monday3 = ""
                print(f"El Lunes Turno 3 de {reservation_name} ha sido eliminado.")
            elif monday4 == reservation_name:
                monday4 = ""
                print(f"El Lunes Turno 4 de {reservation_name} ha sido eliminado.")
            else:
                print("No se encontró un turno con ese nombre el Lunes.")

        # Eliminar turno Martes
        elif reservation_day == 2:
            print(f"Seleccionaste: Martes.")
            reservation_name = input("Ingresa el nombre del paciente que quiere cancelar: ")

            while not reservation_name.isalpha():
                print("Error: solo letras.")
                reservation_name = input("Ingresa nuevamente el nombre del paciente a cancelar: ")

            if tuesday1 == reservation_name:
                tuesday1 = ""
                print(f"El Martes Turno 1 de {reservation_name} ha sido eliminado.")
            elif tuesday2 == reservation_name:
                tuesday2 = ""
                print(f"El Martes Turno 2 de {reservation_name} ha sido eliminado.")
            elif tuesday3 == reservation_name:
                tuesday3 = ""
                print(f"El Martes Turno 3 de {reservation_name} ha sido eliminado.")
            else:
                print("No se encontró un turno con ese nombre el Martes.")

    # Ver agenda del día
    elif menu_option == 3:
        print("1. Lunes")
        print("2. Martes")
        reservation_day = input("Elige un día: ")

        while not reservation_day.isdigit() or int(reservation_day) not in range(1, 3):
            if not reservation_day.isdigit():
                print("Error: no es un número.")
            else:
                print("Error: elección invalida.")
            reservation_day = input("Elige un día: ")

        reservation_day = int(reservation_day)

        if reservation_day == 1:
            print("TURNOS LUNES")
            print("-------------")
            print(f"Turno 1: {'libre' if monday1 == '' else monday1}")
            print(f"Turno 2: {'libre' if monday2 == '' else monday2}")
            print(f"Turno 3: {'libre' if monday3 == '' else monday3}")
            print(f"Turno 4: {'libre' if monday4 == '' else monday4}")

        elif reservation_day == 2:
            print("TURNOS MARTES")
            print("-------------")
            print(f"Turno 1: {'libre' if tuesday1 == '' else tuesday1}")
            print(f"Turno 2: {'libre' if tuesday2 == '' else tuesday2}")
            print(f"Turno 3: {'libre' if tuesday3 == '' else tuesday3}")

    # Ver resumen general
    elif menu_option == 4:
        reservations_monday = 0
        reservations_tuesday = 0
        availables_monday = 0
        availables_tuesday = 0

        # Recuento turnos ocupados y disponibles Lunes
        availables_monday += (monday1 == "")
        reservations_monday += (monday1 != "")

        availables_monday += (monday2 == "")
        reservations_monday += (monday2 != "")

        availables_monday += (monday3 == "")
        reservations_monday += (monday3 != "")

        availables_monday += (monday4 == "")
        reservations_monday += (monday4 != "")

        # Recuento turnos ocupados y disponibles Martes
        availables_tuesday += (tuesday1 == "")
        reservations_tuesday += (tuesday1 != "")

        availables_tuesday += (tuesday2 == "")
        reservations_tuesday += (tuesday2 != "")

        availables_tuesday += (tuesday3 == "")
        reservations_tuesday += (tuesday3 != "")

        busiest_day = "Lunes" if reservations_monday > reservations_tuesday else "Martes" if reservations_tuesday > reservations_monday else "Empate"

        print("RESUMEN GENERAL")
        print("-------------")
        print("LUNES")
        print(f"Turnos ocupados: {reservations_monday}")
        print(f"Turnos disponibles: {availables_monday}")
        print("-------------")
        print("MARTES")
        print(f"Turnos ocupados: {reservations_tuesday}")
        print(f"Turnos disponibles: {availables_tuesday}")
        print("-------------")
        print(f"Día con más turnos: {busiest_day}")

    elif menu_option == 5:
        print("Hasta pronto.")
        break