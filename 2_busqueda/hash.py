def convCad(cad):
	salida = ""
	for l in cad:
		salida += str(ord(l))
	return int(salida)

def hashM(cad, m):
	i = convCad(cad)
	return int(m * (i * 0.00000000212345 % 1))

def agregar(cad, ht, m):
	res = hashM(cad, m)
	ht[res].append(cad)

def buscar(cad, ht, m):
	h = hashM(cad, m)
	for i in ht[h]:
		if i == cad:
			return True
	return False


m = 19
ht = [[] for i in range(m)]

agregar("Hola", ht, m)
agregar("perro", ht, m)
agregar("casa", ht, m)
agregar("leon", ht, m)
print(ht)
res = buscar("libro", ht, m)
print(res)