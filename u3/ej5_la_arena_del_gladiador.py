gladiator_hp = 100
enemy_hp = 100
health_potions = 3
heavy_attack_damage = 15
enemy_attack_damage = 12
gladiator_turn = True

print("---- BIENVENIDO A LA ARENA DEL GLADIADOR ----")

gladiator_name = input("Ingresa tu nombre: ")

while not gladiator_name.isalpha():
    print("¡Error! sólo se permiten letras")
    gladiator_name = input("Ingresa tu nombre: ")

print("==== INICIO DEL COMBATE ====")

# Ciclo de combate
while gladiator_hp > 0 and enemy_hp > 0:

    while gladiator_turn == False:
        print(f"El Enemigo contraataca por {enemy_attack_damage} puntos de daño.")
        gladiator_hp -= enemy_attack_damage
        gladiator_turn = True

    if gladiator_hp <= 0:
        break

    # Mostrar status y menu
    print("---------------------------------------------")
    print(f"{gladiator_name} ({gladiator_hp} HP) vs Enemigo ({enemy_hp} HP) | Pociones: {health_potions}")
    print("---------------------------------------------")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")
    
    menu_option = input("Elige una opción: ")

    while not menu_option.isdigit() or int(menu_option) not in range(1, 4):
        if not menu_option.isdigit():
            print("Error: no es un número.")
        else:
            print("Error: número no válido, debe ser 1, 2 o 3.")
        menu_option = input("Elige una opción: ")

    menu_option = int(menu_option)

    if menu_option == 1:
        final_damage = heavy_attack_damage * 1.5 if enemy_hp < 20 else heavy_attack_damage

        enemy_hp = int(enemy_hp - final_damage)
        print(f"¡Atacaste al enemigo por {final_damage} puntos de daño!")
        gladiator_turn = False  

    elif menu_option == 2:
        print("Inicias una ráfaga de golpes.")
        for i in range(3):
            print("> Golpe conectado por 5 de daño")
            enemy_hp -= 5
        gladiator_turn = False 

    elif menu_option == 3:
        if health_potions > 0:
            gladiator_hp += 30
            health_potions -= 1
            if gladiator_hp > 100:
                gladiator_hp = 100
            gladiator_turn = False 
        else:
            print("¡NO quedan pociones!")
            gladiator_turn = False 

if gladiator_hp > 0:
    print(f"¡VICTORIA! {gladiator_name} ha ganado la batalla.")
elif gladiator_hp <= 0:
    print(f"DERROTA. Has caído en combate.")