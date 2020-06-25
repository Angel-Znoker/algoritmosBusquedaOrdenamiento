"""
	Bubble Sort
	Autor:	Hernandez García Luis Angel

	Algoritmo: Tomando un vector 'a' con elementos a1, a2, ..., an
	1)	Comparar a1 con a2
	2)	Intercambiar si a1 > a2
	3)	Continuar comparando a2 con a3. hasta llegar con a(n-1) vs an
	4)	Repetir el proceso n-1 veces
"""

def bubbleSort(l):
	for i in range(len(l)):
		for j in range(len(l)-1):
			if l[j] > l[j + 1]:
				aux = l[j]
				l[j] = l[j + 1]
				l[j + 1] = aux
	return l

lista = [5, 2, 7, -9, 20, 10, 12, 42456, -7, 57, 6, 3231, 13,]

print(lista)
print(bubbleSort(lista))