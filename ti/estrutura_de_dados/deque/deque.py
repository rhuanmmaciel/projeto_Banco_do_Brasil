import numpy as np


class Deque:
    def __init__(self, capacidade):  # cria o deque com sua capacidade
        self.__capacidade = capacidade
        self.__valores = np.empty(capacidade, dtype=int)
        self.__inicio = 0
        self.__fim = -1
        self.__elementos = 0

    def __vazio(self):  # verifica se o vetor está vazio
        return self.__elementos == 0

    def __cheio(self):  # verifica se o vetor está cheio
        return self.__elementos == self.__capacidade

    def add_inicio(self, valor):  # adiciona no início do vetor
        if self.__cheio():  # verifica se é possível adicionar no início
            print("Fila cheia")
            return False

        self.__elementos += 1  # um elemento a mais

        if self.__inicio == 0:  # se a primeira posição já é o início do vetor, então a posição inicial
                                # deve ser o final do vetor, pois ele funciona de uma forma
                                # circular, exemplo -> 3,4,_,_ -> add_início(9) -> 3,4,_,9
            self.__inicio = self.__capacidade

        self.__inicio -= 1  # a posição inicial será decrescentada em um

        self.__valores[self.__inicio] = valor  # essa posição receberá o valor da função

    def add_fim(self, valor):  # adiciona no final do vetor
        if self.__cheio():  # verifica se é possível adicionar no final
            print("Fila cheia")
            return False

        self.__elementos += 1  # um elemento a mais

        if self.__fim == self.__capacidade - 1:  # se a última posição já é o final do vetor, então a posição final
                                                 # deve ser o início do vetor, pois ele funciona de uma forma
                                                 # circular, exemplo -> _,_,3,4 -> add_fim(9) -> 9,_,3,4
            self.__fim = -1

        self.__fim += 1  # a posição final será acrescentada em um

        self.__valores[self.__fim] = valor  # essa posição receberá o valor da função

    def excluir_inicio(self):  # retira o primeiro item do vetor
        if self.__vazio():  # verifica se está vazio
            print("Fila vazia")
            return False

        self.__elementos -= 1  # -1 elemento

        if self.__inicio == self.__capacidade - 1:  # se o primeiro elemento estiver na última posição, então
                                                    # o novo primeiro elemento será o da primeira posição, por exemplo:
                                                    # 2,3,4,_,_,9 -> excluir_inicio() -> 2,3,4,_,_,_
            self.__inicio = -1

        self.__inicio += 1  # o valor da primeira posição será acrescida em 1

        if self.__elementos == 0:  # caso o número de elementos chegue em 0, o primeiro e o último termo serão
                                   # reinicializados para as posições iniciais
            self.__inicio = 0
            self.__fim = -1

    def excluir_fim(self):  # retira o último valor
        if self.__vazio():  # verifica se está vazio
            print("Fila vazia")
            return False

        self.__elementos -= 1  # -1 elemento

        if self.__fim == 0:                         # se o último elemento estiver na primeira posição, então o
                                                    # novo último elemento será o da última posição,
                                                    # por exemplo: 2,_,_,_,5,9 -> excluir_fim() -> _,_,_,_,5,9
            self.__fim = self.__capacidade

        self.__fim -= 1  # a posição do último item será decrescido em 1

        if self.__elementos == 0:  # caso o número de elementos chegue em 0, o primeiro e o último termo serão
                                   # reinicializados para as posições iniciais
            self.__inicio = 0
            self.__fim = -1

    def ver(self):  # printa o deque inteiro
        print("-----------------")
        k = 1
        for i in range(self.__elementos):  # repetirá de acordo com a quantidade de elementos dentro do vetor
            elemento = i + self.__inicio
            if self.__inicio <= self.__fim:  # caso o valor da posição final seja superior ao valor da posição inicial,
                                             # então o vetor será printado normalmente do início até o fim
                print(f"{k}º elemento: {self.__valores[elemento]} - posição: {elemento}")

            else:  # porém caso contrário a posição i deverá ser decrementada da capacidade quando ela ultrapassá-la,
                   # por exemplo: 0, 1, -, 3, 4 -> o vetor possui 4 elementos, começando na 3ª posição, indo até a 1º
                   # -> quando a variável 'elemento' chegar na posição 5, a qual é inexistente, ela deverá ser
                   # decrescida da capacidade do vetor, portanto -> 5 (elemento) - 5 (capacidade) = 0, logo os valores
                   # lidos serão a partir do elemento 0

                if(elemento >= self.__capacidade):  # verifica se o elemento já está maior que a capacidade
                    elemento -= self.__capacidade  # se estiver, a capacidade é subtraída

                print(f"{k}ª elemento: {self.__valores[elemento]} - posição: {elemento}")

            k += 1

        print("-----------------")

deque = Deque(10)  # teste

deque.add_fim(4)  # 4
deque.add_inicio(3)  # 3 4
deque.add_inicio(2)  # 2 3 4

deque.excluir_fim()  # 2 3

deque.ver()  # 2 3

deque.add_inicio(10)  # 10 2 3
deque.add_inicio(19)  # 19 10 2 3
deque.add_fim(90)  # 19 10 2 3 90
deque.excluir_inicio()  # 10 2 3 90
deque.add_inicio(-5)  # -5 10 2 3 90

deque.ver()  # -5 10 2 3 90
