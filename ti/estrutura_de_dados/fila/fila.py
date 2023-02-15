import numpy as np


class Fila:
    def __init__(self, capacidade):  # inicializa a fila com a sua capacidade e seus atributos
        self.__capacidade = capacidade
        self.__elementos = 0
        self.__primeiro = 0
        self.__ultimo = -1
        self.__valores = np.empty(self.__capacidade, dtype=int)

    def __vazio(self):  # verifica se a fila está vazia
        return self.__elementos == 0

    def __cheio(self):  # verifica se a fila está cheia
        return self.__elementos == self.__capacidade

    def enfileirar(self, valor):  # adiciona um item ao fim da fila
        if self.__cheio():  # verifica se é possível enfileirar
            print("Fila cheia")
            return False

        self.__elementos += 1  # um elemento a mais

        if self.__ultimo == self.__capacidade - 1:  # se a última posição já é o final do vetor, então a posição final
                                                    # deve ser o início do vetor, pois ele funciona de uma forma
                                                    # circular, exemplo -> _,_,3,4 -> enfileirar(9) -> 9,_,3,4
            self.__ultimo = -1

        self.__ultimo += 1  # a posição final será acrescentada em um

        self.__valores[self.__ultimo] = valor  # essa posição receberá o valor da função

    def desenfileirar(self):  # retira o primeiro item do vetor
        if self.__vazio():  # verifica se está vazio
            print("Fila vazia")
            return False

        self.__elementos -= 1  # -1 elemento

        if self.__primeiro == self.__capacidade - 1:  # se o primeiro elemento for o último do vetor, então o primeiro
                                                      # da fila será o primeiro elemento do vetor, por exemplo:
                                                      # 2,3,4,_,_,9 -> desenfileirar() -> 2,3,4,_,_,_
            self.__primeiro = -1

        self.__primeiro += 1  # o valor do primeiro item será acrescido em 1

        if self.__elementos == 0:  # caso o número de elementos chegue em 0, o primeiro e o último termo serão
                                   # reinicializados para as posições iniciais
            self.__primeiro = 0
            self.__ultimo = -1

    def topo(self):  # imprime o valor do 1° termo adicionado
        if self.__vazio():
            print("Fila vazia")
            return
        print(f"Primeiro elemento: {self.__valores[self.__primeiro]}")


fila = Fila(10)  # teste

fila.enfileirar(2)  # 2
fila.enfileirar(3)  # 2 3
fila.enfileirar(4)  # 2 3 4
fila.enfileirar(5)  # 2 3 4 5

print("Teste 1")
fila.topo()  # 2

fila.desenfileirar()  # retira o 2 -> 3 4 5

print("\nTeste 2")
fila.topo()  # 3

fila.enfileirar(2)  # 3 4 5 2
fila.enfileirar(3)  # 3 4 5 2 3
fila.enfileirar(4)  # 3 4 5 2 3 4
fila.enfileirar(5)  # 3 4 5 2 3 4 5

print("\nTeste 3")
fila.topo()  # 3

fila.enfileirar(2)  # 3 4 5 2 3 4 5 2
fila.enfileirar(3)  # 3 4 5 2 3 4 5 2 3
fila.enfileirar(4)  # 3 4 5 2 3 4 5 2 3 4

print("\nTeste 4")
fila.topo()  # 3

fila.desenfileirar()  # retira o 3 -> 4 5 2 3 4 5 2 3 4
fila.desenfileirar()  # retira o 4 -> 5 2 3 4 5 2 3 4
fila.enfileirar(19)  # 5 2 3 4 5 2 3 4 19
fila.desenfileirar()  # retira o 5 -> 2 3 4 5 2 3 4 19

print("\nTeste 5")
fila.topo()  # 2

fila.desenfileirar()  # retira o 2 -> 3 4 5 2 3 4 19
fila.desenfileirar()  # retira o 3 -> 4 5 2 3 4 19
fila.desenfileirar()  # retira o 4 -> 5 2 3 4 19
fila.desenfileirar()  # retira o 5 -> 2 3 4 19
fila.desenfileirar()  # retira o 2 -> 3 4 19
fila.desenfileirar()  # retira o 3 -> 4 19

print("\nTeste 6")
fila.topo() # 4

fila.desenfileirar()  # retira o 4 -> 19

print("\nTeste 7")
fila.topo()  # 19
