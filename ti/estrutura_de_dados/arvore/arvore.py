class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None


class Arvore:
    def __init__(self, valor):
        self.raiz = No(valor)

    def inserir(self, valor):
        aux = self.raiz

        pai = None

        while aux is not None:

            if valor > aux.valor:
                if aux.dir is None:
                    pai = aux
                aux = aux.dir

            else:
                if aux.esq is None:
                    pai = aux
                aux = aux.esq

        if valor > pai.valor:
            pai.dir = No(valor)
        else:
            pai.esq = No(valor)

    def pesquisa(self, valor):
        aux = self.raiz

        while aux.valor != valor:

            if valor > aux.valor:
                aux = aux.dir
            else:
                aux = aux.esq

            if aux is None:
                print("Não existe esse valor")
                return None

        return aux

    def pesquisa_pai(self, valor):
        aux = self.raiz
        pai = None

        while aux.valor != valor:

            pai = aux
            if valor > aux.valor:
                aux = aux.dir
            else:
                aux = aux.esq

            if aux is None:
                print("Não existe esse valor")
                return None

        return pai

    def pre_ordem(self, no):

        if no is not None:
            print(no.valor)
            self.pre_ordem(no.esq)
            self.pre_ordem(no.dir)

    def pos_ordem(self, no):

        if no is not None:
            self.pos_ordem(no.esq)
            self.pos_ordem(no.dir)
            print(no.valor)

    def ordem(self, no):

        if no is not None:
            self.ordem(no.esq)
            print(no.valor)
            self.ordem(no.dir)


arvore = Arvore(6)
arvore.inserir(8)
arvore.inserir(2)
arvore.inserir(1)
arvore.inserir(4)
arvore.inserir(3)

print("----------")
arvore.ordem(arvore.raiz)
print("----------")
arvore.pre_ordem(arvore.raiz)
print("----------")
arvore.pos_ordem(arvore.raiz)
print("----------")
