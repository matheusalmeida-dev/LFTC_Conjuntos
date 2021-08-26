from Conjuntos import *

A = Conjunto(1, 2, 3, 4, 5)
B = Conjunto([1, 2, 3])
C = Conjunto(A)
D = Conjunto()

print("A =", A.getElementos())
print("B =", B.getElementos())
print("C =", C.getElementos())
print("D =", D.getElementos())

print(A.tamanho())
B = Conjunto(1, 2, A)
print("B =", B.getElementos())

print("A contem: ", A.possui(2))
print(A.possui(3))
print(A.possui(10))

print("TESTES CONTÉM")
A = Conjunto(1, 2)
B = Conjunto(1, 2, 3, 4)
C = Conjunto(5, 6, 7)
print(A.contem(A)) # saída é: True
print(B.contem(A)) # saída é: True
print(C.contem(A)) # saída é: False

print("TESTES CONTEM_PROPRIAMENTE")

A = Conjunto(1, 2, 3)
B = Conjunto(1, 2)
print(A.getElementos())
print(B.getElementos())
print(A.contem_propriamente(B)) # saída é: True
print(A.contem_propriamente(A)) # saída é: False
print(B.contem_propriamente(A)) # saída é: False


print('TESTES EH_IGUAL')
A = Conjunto(1, 2)
B = Conjunto(1, 2)
C = Conjunto(1, 2, 3)
print(A.eh_igual(B)) # saída é: True
print(A.eh_igual(C)) # saída é: False

print('TESTES EH_VAZIO')
A = Conjunto(1, 2, 3)
B = Conjunto()
print(A.eh_vazio()) # saída é: False
print(B.eh_vazio()) # saída é: True

print('TESTES UNIÃO')
A = Conjunto(1, 2)
B = Conjunto(1, 2, 3)
C = A.uniao(B) # um novo conjunto com os elementos: 1, 2, 3
print(C.getElementos())

print('TESTES INTERSECAO')
A = Conjunto(1, 2)
B = Conjunto(2, 3, 4)
C = A.intersecao(B) # um novo conjunto com o elemento: 2
print(C.getElementos())

print('TESTES DIFERENÇA')
A = Conjunto(1, 2, 3)
B = Conjunto(1, 4)
C = A.diferenca(B) # um novo conjunto com os elementos: 2, 3
print(C.getElementos())