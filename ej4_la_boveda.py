import random
import string

# Variables iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzados_seguidos = 0

nombre_agente = input("Bienvenido Agente, ingrese su nombre: ")

# Validar nombre
while not nombre_agente.isalpha():
    nombre_agente = input("Error 007: No es un nombre válido, inténtelo nuevamente: ")


while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    

    # Mostrar estado actual y menu
    print(f"Energia: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}")
    print(f"Alarma: {'Activada' if alarma else 'Desactivada'}")

    # Bloqueo por alarma
    if alarma == True and tiempo <= 3:
        break

    print("------------")

    print("1. Forzar cerradura (costo: -20 energía, -2 tiempo)")
    print("2. Hackear panel (costo: -10 energía, -3 tiempo)")
    print("3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra)")

    opcion_menu = input("Elige tu siguiente acción: ")

    while not opcion_menu.isdigit():
        print("Error: no es un número.")
        opcion_menu = input("Elige tu siguiente acción: ")

    opcion_menu = int(opcion_menu)

    while opcion_menu not in range (1, 4):
        print("Error: número no válido.")
        opcion_menu = input("Elige tu siguiente acción: ")
        while not opcion_menu.isdigit():
            print("Error: no es un número.")
            opcion_menu = input("Elige tu siguiente acción: ")
        opcion_menu = int(opcion_menu)
        

    if opcion_menu == 1:

        forzados_seguidos += 1

        # Regla anti-spam
        if forzados_seguidos == 3:
            alarma = True
            energia -= 20
            tiempo -= 2
            forzados_seguidos = 0
        
        elif energia >= 40:
            cerraduras_abiertas += 1
            energia -= 20
            tiempo -= 2
        else:
            opcion_numero = input("Ingresa un número del 1 al 3: ")

            while not opcion_numero.isdigit():
                print("Error: no es un número.")
                opcion_numero = input("Ingresa un número del 1 al 3: ")

            opcion_numero = int(opcion_numero)

            while opcion_numero not in range (1, 4):
                print("Error: número no válido.")
                opcion_numero = input("Ingresa un número del 1 al 3: ")
                while not opcion_numero.isdigit():
                    print("Error: no es un número.")
                    opcion_numero = input("Ingresa un número del 1 al 3: ")
                opcion_numero = int(opcion_numero)

            if opcion_numero == 3:
                alarma = True
                energia -= 20
                tiempo -= 2
                
            else:
                cerraduras_abiertas += 1
                energia -= 20
                tiempo -= 2

    elif opcion_menu == 2:

        energia -= 10
        tiempo -= 3
        forzados_seguidos = 0

        for i in range(1, 5):
            random_letter = random.choice(string.ascii_letters)
            codigo_parcial += random_letter
            print(f"Hackeando... {i}/4")

        print(f"Código encriptado: {codigo_parcial}")

        if len(codigo_parcial) >= 8:
            cerraduras_abiertas += 1
            codigo_parcial = ""

    elif opcion_menu == 3:

        forzados_seguidos = 0

        energia += 15
        tiempo -= 1

        if energia >= 100:
            energia = 100

        if alarma == True:
            energia -= 10

if cerraduras_abiertas == 3:
    print("Victoria.")
elif energia <= 0 or tiempo <= 0:
    print("Derrota")
elif alarma == True and tiempo <= 3:
    print("Derrota (bloqueado)")