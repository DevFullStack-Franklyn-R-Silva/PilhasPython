from pilha import Pilha

def limparExpressao(expressao):
	nova_expressao = ''
 	for c in expressao:
 		if c=='[' or c==']' or c=='(' or c==')':
 			nova_expressao+=c
 	return nova_expressao 

def verificarExpressao(expressao):
 	pilha = Pilha(tamanho =  len(expressao))
 	for c in expressao:
 		if c == '[':
 			pilha.empilhar(']')
 		elif c == '(':
 			pilha.empilhar(')')
 		elif c == ']' and pilha.desempilhar() != ']':
 			return False
 		elif c == ')' and pilha.desempilhar() != ')':
 			return False
 	return True if pilha.estaVazia() else False


expressao = '3-[15+2*(4-3)*[2+(5-1])]/4'
expressao = limparExpressao(expressao)
print(expressao)
print(verificarExpressao(expressao))

