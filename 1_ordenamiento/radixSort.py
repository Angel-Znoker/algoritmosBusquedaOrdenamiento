"""
	Radix Sort
	Autores:	Hernández García Luis Angel
				Vázquez Sánchez Ilse Abril
	
	Este algoritmo realiza el ordenamiento procesando los dígitos de los números
	de forma individual. Para este caso se uso la versión LSD (Least Significant Digit).
	
	Algoritmo:
	1) Asegurarse que todos los números tengan el mismo número de dígitos (se pueden añadir 0's a la izquierda).
	2) Ordenar los numeros por el dígito elegido (iniciando con el menos significativo)
	3) Si quedan dígitos regresar al punto 2 con el siguiente dígito en caso contrario termina el algortimo.
"""
import random

# Función que ejecuta el algoritmo de Radix Sort
def radix(l):
	# (1)
	max = 0 
	for i in l:
		if len(i) > max:
			max = len(i)

	for i in range(len(l)):
		while len(l[i]) < max:
			l[i] = "0"+l[i]

	# (2) y (3)
	for j in range(max-1,-1,-1): # se itera por cada dígito
		ocr = [[] for i in range(10)] # Lista de listas
		# Cada lista tendrá numeros de acuerdo al valor del digito
		for i in range(len(l)):
			ocr[int(l[i][j])].append(l[i])

		l = [] # se limpia la lista original para guardar los números ordenados
		
		# se guardan los numeros ordenados
		for i in range(10):
			l += ocr[i]
	
	return [int(n) for n in l] # se regresa la lista realizando cast a enteros

lista = [str(random.randint(0,200)) for x in range(12)]
print(lista)

lista = radix(lista)
print(lista)