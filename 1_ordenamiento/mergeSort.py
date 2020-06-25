"""	Merge Sort
	Autores: Hernandez Garcia Luis Angel
	
    Basado en la técnica "divide y vencerás". De complejidad O(n log(n)).
	
    Algoritmo:
	1) Si la longitud de la lista es 0 ó 1, ya está ordenado. Si no:
	2) dividir la lista desordenada en dos sublistas de aproximadamente la mitad del tamaño.
	3) Ordenar cada sublista recursivamente aplicando merge sort.
	4) Mexclar las dos sublistas en una sola lista ordenada. """

# Función que realiza las comparaciones para ordenar dos sublistas en una (paso 4)
def merge(l1, l2):
	l3 = [] # Lista vacia para guardar la lista ordenada

	# Ordenamiento de las sublistas
	while(len(l1) > 0 and len(l2) > 0):
		if l1[0] < l2[0]:
			l3.append(l1[0])
			l1 = l1[1:]
		else:
			l3.append(l2[0])
			l2 = l2[1:]

	if len(l1) > 0: # Si quedaron elementos en l1
		l3 = l3 + l1 

	if len(l2) > 0: # Si quedaron elementos en l2
		l3 = l3 + l2

	return l3

# Funcion que realiza la division de la lista para su ordenamiento
# Recibe una lista como parametro
def mergeSort(l):
	# (1)
	if len(l) == 1:
		return l

	# (2)
	li = l[:len(l) // 2]
	ld = l[len(l) // 2:]

	# (3)
	li = mergeSort(li)
	ld = mergeSort(ld)

	# (4)
	return merge(li, ld)

lista = [3, 13, 7, 5,21, 40, 14, 12, 56, 23, 29]

print(lista)
print(mergeSort(lista))