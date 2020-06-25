import math

class Vertice:
	"""Clase que define los vértices de los gráficas"""
	def __init__(self, i, h = 0):
		"""Método que inicializa el vértice con sus atributos
		id = identificador
		heurística = valor definido de la heurística del vértice
		vecinos = lista de los vértices con los que está conectado por una arista
		visitado = flag para saber si fue visitado o no
		padre = vértice visitado un paso antes
		costo = valor que tiene recorrerlo
		costo = de f(n) (especificamente para A*)"""
		self.id = i
		self.heuristica = h
		self.vecinos = []
		self.visitado = False
		self.padre = None
		self.costo = float('inf')
		self.costoF = float('inf')

	def agregarVecino(self, v, p = 0):
		"""Método que agrega los vertices que se encuentre conectados por una arista a la lista de vecinos 
		de un vertice, revisando si éste aún no se encuentra en la lista de vecinos"""
		if v not in self.vecinos:
			self.vecinos.append([v, p])

class Grafica:
	"""Clase que define los vértices de las gráficas"""
	def __init__(self):
		"""vertices = diccionario con los vertices de la grafica"""
		self.vertices = {}

	def agregarVertice(self, id, h = 0):
		"""Método que agrega vértices, recibiendo el índice y la heuristica (para A* puede que no se reciba) revisando si éste no existe en el diccionario
		de vértices"""
		if id not in self.vertices:
			self.vertices[id] = Vertice(id, h)

	def agregarArista(self, a, b, p = 0):
		"""Método que agrega aristas, recibiendo el índice de dos vertices y revisando si existen estos en la lista
		de vertices, además de recibir el peso de la arista , el cual se asigna a ambos vértices por medio del método
		agregar vecino"""
		if a in self.vertices and b in self.vertices:
			self.vertices[a].agregarVecino(b, p)
			self.vertices[b].agregarVecino(a, p)

	def imprimirGrafica(self):
		"""Método que imprime el gráfo completo arista por arista con todas sus características(incluye heurística)"""
		for v in self.vertices:
			print("El costo del vértice "+str(self.vertices[v].id)+" con heuristica "+str(self.vertices[v].heuristica)+" es "+ str(self.vertices[v].costo)+" llegando desde "+str(self.vertices[v].padre))
			
	
	def camino(self, a, b):
		"""Método que va guardando en la lista llamada 'camino' los nodos en el orden que sean visitados y actualizando dicha
		lista con los vértices con el menor costo"""
		camino = []
		actual = b
		while actual != None:
			camino.insert(0, actual)
			actual = self.vertices[actual].padre
		return camino

	def minimoH(self, l):
		"""Método que recibe la lista de los vertices no visitados, revisa si su longitud es mayor a cero(indica que 
		aún hay vértices sin visitar), y realiza comparaciones de los costos de cada vértice en ésta lista para encontrar
		el de menor costo"""
		if len(l) > 0:
			m = self.vertices[l[0]].costoF
			v = l[0]
			for e in l:
				if m > self.vertices[e].costoF:
					m = self.vertices[e].costoF
					v = e
			return v
		return v

	def aEstrella(self, a, b):
		"""Método que sigue el algortimo de Bellman-Ford
		1. Inicialización
			a) Se crea el conjunto_abierto, con el nodo inicial.
			b) Predecesor nulo para todos los nodos. Costo: 0 para inicial 'infinito' para los demás
			c) Costo heurístico: costo + heuristica para el inicial, 'infinito' para el resto
		2. Mientras conjunto abierto tenga elementos
			a) actual <- nodo del conjunto_abierto con menor costo heurístico
			b) si actual = destino, reconstruir camino
			c) Sacar a actual del conjunto abierto y cambiar su estado a visitado
			d) Para cada vecino de actual
				I.	 Si vecino ya está visitado, ignorar y pasar a siguiente
				II.	 Si vecino no esta en conjunto_abierto agregar
				III. Si costo de actual + peso de arista con vecino < costo vecino
					predecesor(vecino) <- actual
					costo(vecino) <- costo(actual) + peso_arista(actual, vecino)
					costo_heuristico(vecino) <- costo(vecino) + heuristica(vecino)
		3. Regresar error
		"""
		if a in self.vertices and b in self.vertices:
			# 1.c
			self.vertices[a].costo = 0
			self.vertices[a].costoF = self.vertices[a].heuristica

			# 1.a y 1.b
			for v in self.vertices:
				if v != a:
					self.vertices[v].costo = float('inf')
					self.vertices[v].costoF = float('inf')
				self.vertices[v].padre = None

			abierto = [a]

			# 2
			while len(abierto) > 0:
				# 2.a
				actual = self.minimoH(abierto)

				# 2.b
				if actual == b:
					return [self.camino(a, b), self.vertices[b].costo, self.vertices[b].heuristica, self.vertices[b].padre]

				# 2.c
				abierto.remove(actual)
				self.vertices[actual].visitado = True

				# 2.d
				for v in self.vertices[actual].vecinos:
					# 2.d.I
					if self.vertices[v[0]].visitado == False:
						# 2.d.II
						if self.vertices[v[0]].id not in abierto:
							abierto.append(v[0])
						# 2.d.III
						if self.vertices[actual].costo + v[1] < self.vertices[v[0]].costo:
							self.vertices[v[0]].padre = actual
							self.vertices[v[0]].costo = self.vertices[actual].costo + v[1]
							self.vertices[v[0]].costoF = self.vertices[v[0]].costo + self.vertices[v[0]].heuristica
			# 3
			return False
		else:
			return False

class main:
	"""Clase principal donde se crean objetos(grafos) de la clase indicada y se llaman sus métodos"""
	# Gráfica 1 A*
	gS = Grafica()
	gS.agregarVertice(0, 55)
	gS.agregarVertice(1, 40)
	gS.agregarVertice(2, 20)
	gS.agregarVertice(3, 40)
	gS.agregarVertice(4, 45)
	gS.agregarVertice(5, 20)
	gS.agregarVertice(6, 0)
	gS.agregarArista(0, 1, 15)
	gS.agregarArista(0, 4, 20)
	gS.agregarArista(1, 2, 20)
	gS.agregarArista(2, 3, 30)
	gS.agregarArista(3, 6, 40)
	gS.agregarArista(4, 5, 30)
	gS.agregarArista(5, 6, 20)
	print("\n\nLa ruta más rápida de G1 por A* junto con su costo es:")
	print(gS.aEstrella(0, 6))
	print("\nLos valores finales de la gráfica G1 por A* son los siguietes:")
	gS.imprimirGrafica()

	#Gráfica 2 A*
	gS1 = Grafica()
	gS1.agregarVertice(0, 17)
	gS1.agregarVertice(1, 15)
	gS1.agregarVertice(2, 12)
	gS1.agregarVertice(3, 5)
	gS1.agregarVertice(4, 0)
	gS1.agregarArista(0, 1, 5)
	gS1.agregarArista(0, 2, 4)
	gS1.agregarArista(0, 3, 11)
	gS1.agregarArista(1, 3, 6)
	gS1.agregarArista(1, 4, 15)
	gS1.agregarArista(2, 3, 5)
	gS1.agregarArista(2, 4, 12)
	gS1.agregarArista(4, 3, 5)
	print("\n\nLa ruta más rápida de G2 por A* junto con su costo es:")
	print(gS1.aEstrella(0, 4))
	print("\nLos valores finales de la gráfica G2 por A* son los siguietes:")
	gS1.imprimirGrafica()