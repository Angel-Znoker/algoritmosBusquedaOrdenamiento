# clase que define un vertice
class Vertice:
	# constructor
	def __init__(self, i):
		self.id = i
		self.visitado = False
		self.padre = None
		self.vecinos = []

	def agregarVecino(self, v):
		if v not in self.vecinos:
			self.vecinos.append(v)

# clase que define a una gráfica
class Grafica:
	def __init__(self):
		self.vertices = {}

	def agregarVertice(self, v):
		if v not in self.vertices:
			self.vertices[v] = Vertice(v)

	def agregarArista(self, a, b):
		if a in self.vertices and b in self.vertices:
			self.vertices[a].agregarVecino(b)
			self.vertices[b].agregarVecino(a)

	def dfs(self, r):
		self.vertices[r].visitado = True

		for v in self.vertices[r].vecinos:
			if self.vertices[v].visitado == False:
				self.vertices[v].padre = r
				print("(" + str(v) + ", " + str(r) + ")")
				self.dfs(v)

def Main():
	g = Grafica()

	# lista de vértices 
	l = [0, 1, 2, 3, 4, 5, 6]
	for n in l:
		g.agregarVertice(n)

	# lista de aristas. Cada par de numeros es una arista (union entre dos vértices)
	l = [2,5, 2,3, 3,4, 3,5, 5,6, 6,4, 4,1 ]
	for i in range(0, len(l) - 1, 2):
		g.agregarArista(l[i], l[i + 1])

	for v in g.vertices:
		print(v, g.vertices[v].vecinos)

	print("\n\n")

	g.dfs(2)

Main()