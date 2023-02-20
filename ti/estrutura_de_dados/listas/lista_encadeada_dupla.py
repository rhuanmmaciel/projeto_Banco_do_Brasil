class No:
    def __init__(self, valor):

        self.valor = valor
        self.proximo = None
        self.anterior = None

    def ver_no(self):

        print(self.valor)


class Lista:
    def __init__(self):

        self.__primeiro = None
        self.__ultimo = None

    def inserir_posicao(self, valor, posicao):

        if posicao >= self.tamanho():
            self.inserir_final(valor)
            return

        if posicao == 0:
            self.inserir_inicio(valor)
            return

        anterior = self.no(posicao - 1)
        proximo = self.no(posicao)

        no = No(valor)

        anterior.proximo = no
        no.anterior = anterior

        proximo.anterior = no
        no.proximo = proximo
        self.atualizar_ultimo()

    def inserir_inicio(self, valor):

        no = No(valor)

        proximo = self.__primeiro
        no.proximo = proximo
        if proximo is not None:
            proximo.anterior = no

        self.__primeiro = no

        self.atualizar_ultimo()

    def inserir_final(self, valor):

        no = No(valor)
        no.proximo = None
        aux = self.__primeiro

        if aux is None:
            self.inserir_inicio()
            return

        while aux.proximo is not None:
            aux = aux.proximo

        aux.proximo = no
        no.anterior = aux

        self.atualizar_ultimo()

    def atualizar_ultimo(self):
        aux = self.__primeiro
        while aux.proximo is not None:
            aux = aux.proximo

        self.__ultimo = aux

    def possui(self, valor):

        aux = self.__primeiro
        posicao = 0
        while aux is not None:
            if aux.valor == valor:
                return posicao
            posicao += 1
            aux = aux.proximo

        return None

    def excluir(self, valor):

        posicao = self.possui(valor)
        if posicao is None:
            print("Não existe esse valor na lista")
            return

        if posicao == 0:
            self.__primeiro = self.__primeiro.proximo
            self.__primeiro.anterior = None
            self.atualizar_ultimo()
            return

        atual = self.no(posicao)
        anterior = self.no(posicao - 1)
        anterior.proximo = atual.proximo
        atual.proximo.anterior = anterior

        self.atualizar_ultimo()

    def no(self, posicao):

        if posicao + 1 > self.tamanho():
            return None

        aux = self.__primeiro
        for i in range(posicao):
            aux = aux.proximo
        return aux

    def tamanho(self):

        aux = self.__primeiro
        contador = 0
        while aux is not None:
            contador += 1
            aux = aux.proximo

        return contador

    def ver_lista(self):

        print("------------------")
        aux = self.__primeiro

        while aux is not None:
            aux.ver_no()
            aux = aux.proximo

        print("------------------")


lista = Lista()

lista.inserir_inicio(4)
lista.inserir_inicio(2)
lista.inserir_final(5)
lista.inserir_inicio(9)

lista.inserir_posicao(11, 3)

lista.ver_lista()
print(f"Anterior da posição 3: {lista.no(3).anterior.valor}")
