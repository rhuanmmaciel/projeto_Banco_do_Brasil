import numpy as np


class Pilha:  # classe que implementa uma pilha
    def __init__(self, capacidade):  # inicializa a pilha com a sua capacidade designada
        self.__capacidade = capacidade
        self.__topo = -1  # como não há valor na inicialização, o topo dela é uma posição não existente -1
        self.__valores = np.chararray(self.__capacidade, unicode=True)

    def __pilha_vazia(self):  # verifica se a pilha está vazia
        return self.__topo == -1

    def __pilha_cheia(self):  # verifica se a pilha está cheia
        return self.__topo == self.__capacidade - 1

    def empilhar(self, valor):  # empilha os itens
        if self.__pilha_cheia():  # se a pilha estiver cheia não é possível empilhar
            print("A pilha está cheia")
            return
        self.__topo += 1  # o topo se torna uma posição acima quando empilhado algo
        self.__valores[self.__topo] = valor  # esse topo receberá o valor passado na função

    def desempilhar(self):  # desempilha os itens
        if self.__pilha_vazia():
            return False
        self.__topo -= 1  # a pilha retrocede um valor quando um item for desempilhado
        return self.__valores[self.__topo + 1]  # é retornado esse valor desempilhado caso queira utilizá-lo

    def ver_pilha(self):  # imprime todos elementos da pilha
        if self.__pilha_vazia():
            print("A pilha está vazia")
            return
        print("-----------------")
        for i in range(self.__topo + 1):
            print(f"{i+1}º termo: {self.__valores[i]} ")
        print("-----------------")


pilha = Pilha(10)  # testes
pilha.empilhar(2)
pilha.empilhar(0)
pilha.empilhar(3)
pilha.empilhar(7)
pilha.empilhar(20)

pilha.ver_pilha()

pilha.desempilhar()
pilha.desempilhar()

pilha.ver_pilha()
