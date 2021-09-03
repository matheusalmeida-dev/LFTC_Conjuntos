from Conjuntos import *
Z = Conjunto('a', 'b')
A = Conjunto(1, 2, 3, 4, 5)
B = Conjunto([1, 2, 3], [3, 4])
C = Conjunto(A)
D = Conjunto()
E = Conjunto(1, 2, A)
F = Conjunto( 1, 'x', A, Z, ['v', 'b'])


print("A =", A.string())
print("B =", B.string())
print("C =", C.string())
print("D =", D.string())
print("E =", E.string())
print("F =", F.string())

print(A.tamanho())
B = Conjunto(1, 2, A)
print("B =", B.string())

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
print(A.string())
print(B.string())
print(A.contem_propriamente(B)) # saída é: True
print(A.contem_propriamente(A)) # saída é: False
print(B.contem_propriamente(A)) # saída é: False


print('TESTES EH_IGUAL')
A = Conjunto(1, 2)
B = Conjunto(2, 1)
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
print(C.string())

print('TESTES INTERSECAO')
A = Conjunto(1, 2)
B = Conjunto(2, 3, 4)
C = A.intersecao(B) # um novo conjunto com o elemento: 2
print(C.string())

print('TESTES DIFERENÇA')
A = Conjunto(1, 2, 3)
B = Conjunto(1, 4)
C = A.diferenca(B) # um novo conjunto com os elementos: 2, 3
print(C.string())

print("TESTES COMPLEMENTO")
U = Conjunto(1, 2, 3, 4, 5)
A = Conjunto(1, 2)
C = A.complemento(U) # um novo conjunto com os elementos: 3, 4, 5
print(C.string())

print("TESTES CONJUNTO_DAS_PARTES")
A = Conjunto(1, 2, 3)
P = A.conjunto_das_partes()
print(P.string())
# P é um novo conjunto com os elementos:
# Conjunto(), 
# Conjunto(1), Conjunto(2), Conjunto(3), 
# Conjunto(1, 2), Conjunto(1, 3), Conjunto(2, 3), 
# Conjunto(1, 2, 3)