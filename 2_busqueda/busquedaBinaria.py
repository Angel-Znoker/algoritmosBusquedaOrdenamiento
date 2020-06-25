def busBin(l, x):
	if(len(l) > 0):
		lc = l[len(l) // 2]

		if x == lc :
			return True

		else:
			if(x < lc):
				return busBin(l[:len(l) // 2], x)

			else:
				return busBin(l[len(l) // 2 + 1:], x)

	else:
		return False

lista = [1, 2, 10, 20, 25, 60, 100, 150]
resultado = busBin(lista, 60)
print(resultado)