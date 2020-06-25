import math

class Vertice:
	"""Clase que define los vértices de los gráficas"""
	def __init__(self, i):
		"""Método que inicializa el vértice con sus atributos
		id = identificador
		vecinos = lista de los vértices con los que está conectado por una arista
		visitado = flag para saber si fue visitado o no
		padre = vértice visitado un paso antes
		costo = valor que tiene recorrerlo"""
		self.id = i
		self.vecinos = []
		self.visitado = False
		self.padre = None
		self.costo = float('inf')

	def agregarVecino(self, v, p):
		"""Método que agrega los vertices que se encuentre conectados por una arista a la lista de vecinos 
		de un vertice, revisando si éste aún no se encuentra en la lista de vecinos"""
		if v not in self.vecinos:
			self.vecinos.append([v, p])

class Grafica:
	"""Clase que define los vértices de las gráficas"""
	def __init__(self):
		"""vertices = diccionario con los vertices de la grafica"""
		self.vertices = {}

	def agregarVertice(self, id):
		"""Método que agrega vértices, recibiendo el índice y la heuristica (para A* puede que no se reciba) revisando si éste no existe en el diccionario
		de vértices"""
		if id not in self.vertices:
			self.vertices[id] = Vertice(id)

	def agregarArista(self, a, b, p):
		"""Método que agrega aristas, recibiendo el índice de dos vertices y revisando si existen estos en la lista
		de vertices, además de recibir el peso de la arista , el cual se asigna a ambos vértices por medio del método
		agregar vecino"""
		if a in self.vertices and b in self.vertices:
			self.vertices[a].agregarVecino(b, p)
			self.vertices[b].agregarVecino(a, p)

	def imprimirGrafica(self):
		"""Método que imprime el gráfo completo arista por arista con todas sus características(incluye heurística)"""
		for v in self.vertices:
			print("El costo del vértice "+str(self.vertices[v].id)+" es "+ str(self.vertices[v].costo)+" llegando desde "+str(self.vertices[v].padre))
			
	
	def camino(self, a, b):
		"""Método que va guardando en la lista llamada 'camino' los nodos en el orden que sean visitados y actualizando dicha
		lista con los vértices con el menor costo"""
		camino = []
		actual = b
		while actual != None:
			camino.insert(0, actual)
			actual = self.vertices[actual].padre
		return [camino, self.vertices[b].costo]

	def bellmanFord(self, a):
		"""Método que sigue el algortimo de Bellman-Ford
		1. Asignar a cada nodo una distancia y un nodo predecesor tentativos: 0 para el nodo inicial e infinito para todos los restantes, predecesor nulo para todos los nodos
		2. Repetir |V| - 1 veces
			a)Para cada arista (u, v) con peso w: si la distancia del nodo actual u sumada al peso w de la arista que llega a v es menor que la distancia tentativa a v, 
			sobreescribir la distancia a v con la suma mencionada y guardar a u como predecesor de v
		3. Verificar que no existan ciclos de pesos negativos
			a) Para cada arista (u, v) con peso w: si la distancia del nodo actual u sumada al peso w de la arista que llega a v es menor que la distancia tentativa a v, mandar 
		un mensaje de error indicando que existe un ciclo de peso negativo	
		"""
		# 1
		if a in self.vertices:
			self.vertices[a].costo = 0

			for v in self.vertices:
				if v != a:
					self.vertices[v].costo = float('inf')
				self.vertices[v].padre = None

			# 2
			for x in range(len(self.vertices) - 1):
				# 2.a
				for actual in self.vertices:
					for vec in self.vertices[actual].vecinos:
						if self.vertices[actual].costo + vec[1] < self.vertices[vec[0]].costo:
							self.vertices[vec[0]].costo = self.vertices[actual].costo + vec[1]
							self.vertices[vec[0]].padre = actual

			# 3
			for actual in self.vertices:
				# 3.a
				for vec in self.vertices[actual].vecinos:
					if self.vertices[actual].costo + vec[1] < self.vertices[vec[0]].costo:
						return "Error: Existe un ciclo con peso negativo en la gráfica"

		else:
			return False

class main:
	"""Clase principal donde se crean objetos(grafos) de la clase indicada y se llaman sus métodos"""
	g = Grafica()
	g.agregarVertice(1)
	g.agregarVertice(2)
	g.agregarVertice(3)
	g.agregarVertice(4)
	g.agregarVertice(5)
	g.agregarVertice(6)
	g.agregarArista(1, 6, 14)
	g.agregarArista(1, 2, 7)
	g.agregarArista(1, 3, 9)
	g.agregarArista(2, 3, 10)
	g.agregarArista(2, 4, 15)
	g.agregarArista(3, 4, 11)
	g.agregarArista(3, 6, 2)
	g.agregarArista(4, 5, 6)
	g.agregarArista(5, 6, 9)

	print("\n\nLa ruta más rápida por Bellman-Ford junto con su costo es:")
	g.bellmanFord(1)
	print(g.camino(1, 6))
	print("\nLos valores finales de la gráfica son los siguietes:")
	g.imprimirGrafica()