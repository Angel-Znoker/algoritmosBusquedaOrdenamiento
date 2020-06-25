"""
	Heapsort
	Autor: Hernández García Luis Angel

	De complejidad O(n log(n)). Para realizar este ordenamiento se deben de acomodar
	a la lista de numeros en montículos (heaps), un nodo con dos hijos (formando un árbol
	binario) y debe de cumplir que el padre debe ser el mayor (o menor) de los tres
	numeros. De esta forma, al inicio de la lista siempre se encontrará el numero mayor
	(o menor).
"""

# Esta función se encarga de acomodar a un heap con el padre menor
# que los hijos. Recibe una lista y la posición del padre del heap.
def heapifyRecursivo(l, i):
	# Se verifica si el numero en la posición dada tiene dos hijos
	if 2 * i + 2 <= len(l) - 1:
		if l[2 * i + 1] <= l[2 * i + 2]: # se busca el menor de los hijos
			min = 2 * i + 1
		else:
			min = 2 * i + 2

		# se compara el valor del menor de los hijos con el valor del nodo padre
		# y se intercambia de ser necesario
		if l[i] > l[min]: 
			aux = l[i]
			l[i] = l[min]
			l[min] = aux

			# se realiza el heapify con el nodo intercambiado
			l = heapifyRecursivo(l, min)

	# se verifica si el nodo tiene un hijo por lo menos
	elif 2 * i + 1 <= len(l) - 1:
		# si el hijo es menor que el padre se realiza el intercambio
		if l[i] > l[2 * i + 1]:
			aux = l[i]
			l[i] = l[2 * i + 1]
			l[2 * i + 1] = aux

			# se realiza el heapify con el nodo intercambiado
			l = heapifyRecursivo(l, 2 * i +1)

	return l

# Esta función se encarga de acomodar los numeros en orden
# cada vez que manda a llamar a cada heapify. Recibe una lista.
def heapsort(l):
	# Se hace el acomodo inicial, desde el último padre al primero
	for i in range(len(l) // 2 - 1, -1, -1):
		l = heapifyRecursivo(l, i)

	l2 = [] # lista que almacena los numeros en orden

	for i in range(0, len(l)):
		# se intercambia el numero que esta al final de la lista con
		# el primero (el menor)
		aux = l[0]
		l[0] = l[len(l) - 1]
		l[len(l) - 1] = aux

		l2.append(aux) # se guarda el menor numero

		l = l[:len(l) - 1] # se elimina el numero menor de la lista
		l = heapifyRecursivo(l, 0) # se realiza el heapify

	return l2

lista = [0, 10, 2, 5, 6, 2, -1, -5, 7, 225, -15]
print(lista)

lista = heapsort(lista)
print(lista)