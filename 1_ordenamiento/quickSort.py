"""	Quick Sort
	Autores: Hernandez Garcia Luis Angel

	Basado en la técnica "divide y vencerás".
	
	Algoritmo:
	1) Si la longitud de la lista es 0 ó 1, ya está ordenado. Si no:
	2) Elegir un elemento del arreglo como pivote.
	3) Reubicar los demás elementos de la lista a cada lado del pivote; del lado izquierdo los menores y del derecho los mayores (o viceversa).
	4) Repetir el proceso recursivamente para cada sublista, sin tomar al pivote.
	5) Retornar la sublista izquierda, pivote y sublista derecha; en ese orden
"""

def quickSort(l):
	# (1)
	if len(l) <= 1:
		return l
	
	# (2)
	piv = l[len(l) - 1]
	l.pop()

	# (3)
	l1 = [n for n in l if n <= piv]
	l2 = [n for n in l if n > piv]

	# (4)
	l1 = quickSort(l1)
	l2 = quickSort(l2)

	# (5)
	return l1 + [piv] + l2

lista = [9, -3, 5, 2, 6, 8, -6, 1, 3]

print(lista)
print(quickSort(lista))