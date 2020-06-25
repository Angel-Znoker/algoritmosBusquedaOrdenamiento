def busLin(l, x):
	for i in l:
		if i == x:
			return i

	return None

lista = [-5, -1, 2, 2, 5, 6, 10, 27]

print(busLin(lista, int(input())))