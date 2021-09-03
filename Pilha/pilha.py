class Pilha:
	itens = None
	topo = None
	tam = None

	#iniciar pilha
	def __init__(self,tam):
		self.tam = tam
		self.topo = 0
		self.itens = [None]*tam

	#verificar se esta vazia
	def estaVazia(self):
		return True if self.topo == 0 else False

	#verificar se esta cheia
	def estaCheia(self):
		return True if self.topo == self.tam else False

	#empilhar
	def empilhar(self,item):
		if not self.estaCheia():
			self.itens[self.topo] = item
			self.topo += 1
		else:
			print('esta cheia')

	#desempilhar
	def desempilhar(self):
		if not self.estaVazia():
			self.topo -=1
			return self.itens[self.topo]
		else:
			print('esta vazia')

	def contemItem(self,item):
		for i in reversed(self.itens[:self.topo]):
			if item == i:
				return True
		return False

	#imprimir
	def imprimir(self):
		[print(item) for item in reversed(self.itens[:self.topo])]
		print('----')