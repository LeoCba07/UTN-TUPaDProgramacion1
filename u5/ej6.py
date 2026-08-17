lista = [1, 3, 6, 7, 4, 20, 11]

lista[:] = lista[-1:] + lista[:-1]

print(lista)