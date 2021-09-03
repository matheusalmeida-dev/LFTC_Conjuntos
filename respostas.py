from Conjuntos import *

A = Conjunto(1, 2, 3)
B = Conjunto('a', 'b', 'c')
C = Conjunto(1, 2, 4, 5)
D = Conjunto(A, 1, 2)
E = Conjunto(B, C)


U = Conjunto()
U = A.uniao(B).uniao(C).uniao(D).uniao(E)
print(U.string())

print('\nQuestão 1')
X = A.uniao(B).uniao(C)
print(X.string())

print('\nQuestão 2')
X = A.intersecao(C)
print(X.string())

print('\nQuestão 3')
X = A.complemento(U)
print(X.string())

print('\nQuestão 4')
X = B.uniao(D).complemento(U)
print(X.string())

print('\nQuestão 5')
X = U.intersecao(A)
print(X.string())

print('\nQuestão 6')
X = C.diferenca(A)
print(X.string())

print('\nQuestão 7')
print(A.contem(C))

print('\nQuestão 8')
print(A.contem_propriamente(C))

print('\nQuestão 9')
print(A.eh_igual(B))

print('\nQuestão 10')
X = A.conjunto_das_partes()
print(X.string())

print('\nQuestão 11')
X = D.conjunto_das_partes()
print(X.string())

print('\nQuestão 12')
X = A.produto_cartesiano(B)
print(X.string())

print('\nQuestão 13')
X = A.produto_cartesiano(E)
print(X.string())
