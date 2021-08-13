class Conjunto:
    def __init__(self, *args):
        self.elementos = []
        for item in args:
            if isinstance(item, list):
                for item2 in item:
                    self.elementos.append(item2)
            elif isinstance(item, Conjunto):
                self.elementos += item.elementos
            else:
                self.elementos.append(item)

    def tamanho(self):
        print(len(self.elementos))

    def getElementos(self):
        return self.elementos

    def possui(self, valor):
        for elemento in self.elementos:
            if valor == elemento:
                return True
        return False

    def contem(self, conjunto):
        for elemento in conjunto.elementos:
            if not self.possui(elemento):
                return False
        return True

    def contem_propriamente(self, conjunto):
        for elemento in conjunto.elementos:
            if not self.possui(elemento):
                return False
        for elemento in self.elementos:
            if not conjunto.possui(elemento):
                return True
        return False

'- - - - - - -'

A = Conjunto(1, 2, 3, 4, 5)
B = Conjunto([1, 2, 3])
C = Conjunto(A)
D = Conjunto()

print("A =", A.getElementos())
print("B =", B.getElementos())
print("C =", C.getElementos())
print("D =", D.getElementos())

A.tamanho()
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