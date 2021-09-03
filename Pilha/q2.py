from pilha import Pilha

def limparExpressao(expressao):
	nova_exp = ''
	for i in range(len(expressao)):
		if expressao[i]=='[' or expressao[i]=='(' or expressao[i]==')' or expressao[i]==']':
			nova_exp += expressao[i]
	return nova_exp	

def ehBemFormada(expressao):
	expressao = limparExpressao(expressao)
	print(expressao)
	if len(expressao)%2!=0:
		return False
	else:
		pilha = Pilha(int(len(expressao)/2))
		for i in range(len(expressao)):
			if expressao[i] == '[':
				pilha.empilhar(']')
			elif expressao[i] == '(':
				pilha.empilhar(')')
			elif expressao[i] == ']':
				if pilha.desempilhar() != ']':
					return False
			elif expressao[i] == ')':
				if pilha.desempilhar() != ')':
					return False
		return True if pilha.estaVazia() else False
		

expressao = '3+[['#'3-[15+2*(4-3)*[2+(5-1)]]/4'
print(ehBemFormada(expressao))






































# from pilha import Pilha

# sentenca = 'A dama admirou o rim da amada'
# # retirar espacos
# sentenca = sentenca.replace(' ','').lower()

# def palindromo(sentenca):
# 	pilha = Pilha(len(sentenca)//2)

# 	if(len(sentenca)%2!=0):
# 		sentenca = sentenca[0:len(sentenca)//2]+sentenca[len(sentenca)//2+1:]

# 	i = 0
# 	while i < len(sentenca):
# 		if i < len(sentenca)//2:
# 			pilha.empilhar(sentenca[i])
# 		else:
# 			letra = pilha.desempilhar()
# 			if letra != sentenca[i]:
# 				return False
# 		i +=1
# 	return True

# print(palindromo(sentenca))