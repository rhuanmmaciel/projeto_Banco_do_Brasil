import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype=int)

    def __pilha_vazia(self):
        return self.__topo == -1

    def __pilha_cheia(self):
        return self.__topo == self.__capacidade - 1

    def empilhar(self, valor):
        if self.__pilha_cheia():
            print("A pilha está cheia")
            return
        self.__topo += 1
        self.__valores[self.__topo] = valor

    def desempilhar(self):
        if self.__pilha_vazia():
            print("A pilha já está vazia")
            return
        self.__topo -= 1

    def ver_pilha(self):
        if self.__pilha_vazia():
            print("A pilha está vazia")
            return
        print("-----------------")
        for i in range(self.__topo + 1):
            print(f"{i+1}º termo: {self.__valores[i]} ")
        print("-----------------")


pilha = Pilha(10)
pilha.empilhar(2)
pilha.empilhar(0)
pilha.empilhar(3)
pilha.empilhar(7)
pilha.empilhar(20)

pilha.ver_pilha()

pilha.desempilhar()
pilha.desempilhar()

pilha.ver_pilha()
