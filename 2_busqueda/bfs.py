# clase que define a un vertice en general
class Vertice:
	# constructor
	def __init__(self, i):
		self.id = i
		self.visitado = False # para algunos recorridos o búsquedas
		self.nivel = -1
		self.vecinos = [] # conexión con otros nodos

	def agregarVecino(self, v):
		if v not in self.vecinos:
			self.vecinos.append(v)

# clase que define a una gráfica
class Grafica:
	def __init__(self):
		self.vertices = {}

	def agregarVertice(self, v):
		if v not in self.vertices:
			# vertices que tendrá la gráfica
			self.vertices[v] = Vertice(v)

	def agregarArista(self, a, b):
		if a in self.vertices and b in self.vertices:
			self.vertices[a].agregarVecino(b)
			self.vertices[b].agregarVecino(a)

	def bfs(self, r):
		if r in self.vertices:
			cola = [r]

			self.vertices[r].visitado = True
			self.vertices[r].nivel = 0

			print("(" + str(r) + ", " + str(self.vertices[r].nivel) + ")")

			while len(cola) > 0:
				act = cola[0]
				cola = cola[1:]
				for v in self.vertices[act].vecinos:
					if self.vertices[v].visitado == False:
						cola.append(v)
						self.vertices[v].visitado = True
						self.vertices[v].nivel = self.vertices[act].nivel + 1
						print("(" + str(v) + ", " + str(self.vertices[v].nivel) + ")")
		else:
			print("Vertice inexistente")

def Main():
	g = Grafica()

	# lista de vértices 
	l = [0, 1, 2, 3, 4, 5, 6]
	for n in l:
		g.agregarVertice(n)

	# lista de aristas. Cada par de numeros es una arista (union entre dos vértices)
	l = [1, 4, 4, 3, 4, 6, 3, 5, 3, 2, 6, 5, 5, 2]
	for i in range(0, len(l) - 1, 2):
		g.agregarArista(l[i], l[i + 1])

	for v in g.vertices:
		print(v, g.vertices[v].vecinos)

	print("\n\n")

	g.bfs(2)

Main()