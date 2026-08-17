import random

# Generamos una lista de 15 números entre 1 y 100
random_numbers = random.sample(range(1, 101), 15)

# Creamos una lista para los numeros pares y otra para los impares
evens_list = [x for x in random_numbers if x % 2 == 0]
odds_list = [x for x in random_numbers if x % 2 != 0]

print(f"Hay {len(evens_list)} números pares")
print(f"Hay {len(odds_list)} números impares")
print(f"Los números eran {random_numbers}")
