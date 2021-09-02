from itertools import combinations

def ordem(e):
    return len(e.getElementos())

class Conjunto:
    def __init__(self, *args):
        self.elementos = []
        for item in args:
            if isinstance(item, list) or isinstance(item, tuple):
                self.elementos += list(item)
            elif isinstance(item, Conjunto):
                self.elementos += item.elementos
            else:
                self.elementos.append(item)
        self.elementos = list({k: None for k in self.elementos}.keys())

    def tamanho(self):
        return len(self.elementos)

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

    def eh_igual(self, conjunto):
        return self.elementos == conjunto.elementos

    def eh_vazio(self):
        return self.elementos == []
    
    def uniao(self, conjunto):
        return Conjunto(self, conjunto)

    def intersecao(self, conjunto):
        aux = []
        for elemento in self.elementos:
            if elemento in conjunto.elementos:
                aux.append(elemento)
        return Conjunto(aux)

    def diferenca(self, conjunto):
        aux = []
        for elemento in self.elementos:
            if not elemento in conjunto.elementos:
                aux.append(elemento)
        return Conjunto(aux)

    def complemento(self, conjunto):
        return Conjunto(list(set(conjunto.elementos)-set(self.elementos)))

    def conjunto_das_partes(self):
        itens = self.getElementos()
        n = 1
        aux = []
        aux.append(Conjunto([]))
        while n <= self.tamanho():
            lista = combinations(itens, n)
            for item in lista:
                aux.append(Conjunto(item))
            n += 1
        return Conjunto(aux)
