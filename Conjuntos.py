from itertools import combinations, product

def ordem(e):
    return len(e.getElementos())

class Conjunto:
    def __init__(self, *args):
        self.elementos = []
        for item in args:
            if isinstance(item, list) or isinstance(item, tuple):
                for elemento in item:
                    self.elementos.append(elemento)
            elif isinstance(item, Conjunto):
                if not self.elementos:
                    self.elementos += item.elementos
                else:
                    self.elementos.append(item)
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
        if self.contem(conjunto):
            for elemento in self.elementos:
                if not conjunto.possui(elemento):
                    return True
        return False

    def eh_igual(self, conjunto):
        for elemento in self.elementos:
                if not conjunto.possui(elemento):
                    return False
        for elemento in conjunto.elementos:
                if not self.possui(elemento):
                    return False
        return True

    def eh_vazio(self):
        return self.elementos == []
    
    def uniao(self, conjunto):
        lista = []
        for item in conjunto.elementos:
            if isinstance(item, Conjunto):
                item.uniao(item)
            else:
                lista.append(item)
        return Conjunto(self, lista)

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
        aux = []
        for elemento in conjunto.elementos:
            if not elemento in self.elementos:
                aux.append(elemento)
        return Conjunto(aux)

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

    def produto_cartesiano(self, conjunto):
        itens = self.getElementos()
        aux = []
        lista = product(itens, conjunto.elementos)
        for item in lista:
            aux.append(item)
        return Conjunto(aux)


    def string(self):
        resposta = '{'
        for item in self.elementos:
            if isinstance(item, list):
                for elemento in item:
                    if not isinstance(elemento, Conjunto):
                        resposta += str(elemento) + ', '
                    else:
                        resposta += item.string()
            elif isinstance(item, Conjunto):
                resposta += item.string() + ', '
            else:
                if isinstance(item, tuple) and len(item)== 1:
                    resposta += str(item[0]) + ', '
                elif isinstance(item, tuple):
                    resposta += '('
                    for elemento in item:
                        if isinstance(elemento, Conjunto):
                            resposta += elemento.string()
                        else:
                            resposta += str(elemento) + ', '
                    resposta += '), '
                else:
                    resposta += str(item) + ', '
        resposta += '}'
        return resposta.replace(', }', '}').replace(', )', ')')