from pilha import Pilha

#empilhar container
def empilhar(container,pilhas):
	menor_pilha = pilhas[0]
	for pilha in pilhas[1:4]:
		if pilha.topo<menor_pilha.topo:
			menor_pilha = pilha


#desempilhar container

pilhas = [Pilha(5),Pilha(5),Pilha(5),Pilha(5),Pilha(5)]
containers = ['c1','c2','c3','c4','c5','c6','c7','c8','c9','c10']

empilhar('c1',pilhas)

































# from pilha import Pilha

# def inserir(container,pilhas):
# 	menor_pilha = pilhas[0]
# 	for p in pilhas[1:len(pilhas)-1]:
# 		menor_pilha = p if p.topo < menor_pilha.topo else menor_pilha
# 	if not menor_pilha.estaCheia():
# 		menor_pilha.empilhar(container)

# def imprimir(pilhas):
# 	i = 0
# 	for p in pilhas:
# 		print('pilha ',i)
# 		p.imprimir()
# 		i+=1

# def desempilhar(container,pilhas):
# 	#encontrar container
# 	i = 0
# 	while i < len(pilhas) and not pilhas[i].contemItem(container):
# 		i+=1
# 	if i < len(pilhas):
# 		p = pilhas[i]
# 		c = p.desempilhar()
# 		while c != container:
# 			pilhas[4].empilhar(c)
# 			c = p.desempilhar()
# 		if c == container:
# 			while not pilhas[4].estaVazia():
# 				p.empilhar(pilhas[4].desempilhar())
# 		return c
# 	else:
# 		return 'nao existe container'

# pilhas = [Pilha(5),Pilha(5),Pilha(5),Pilha(5),Pilha(5)]

# containers = ['c1','c2','c3','c4','c5','c6','c7','c8','c9','c10']

# for c in containers:
# 	inserir(c,pilhas)

# imprimir(pilhas)

# desempilhar('c6',pilhas)
# print('\n')
# imprimir(pilhas)



