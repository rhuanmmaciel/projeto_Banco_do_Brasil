import numpy as np


class vetor:

    # quando criamos um vetor é necessário informar sua capacidade, pois essa estrutura aloca memória estaticamente
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1  # atributo que nos permite saber a última posição existente do vetor, caso -1 o
        # vetor é nulo
        self.array = np.empty(self.capacidade, dtype=int)  # criação do vetor passando a capacidade e o tipo de dados

    # impressão do vetor sempre verificando se ele não é vazio
    def imprime(self):
        if self.ultima_posicao <= -1:
            print("Array vazio")
        else:
            print("-------------------")
            for i in range(self.ultima_posicao + 1):
                print(str(i) + " - " + str(self.array[i]))
            print("-------------------")

    # inserir no vetor caso ele não esteja cheio e atualizando a variável que indica a última posição
    def insere(self, valor):
        if self.ultima_posicao + 1 == self.capacidade:
            print("Array cheio")
        else:
            self.ultima_posicao += 1  # agora que inserimos um dado o array está maior em uma unidade
            self.array[self.ultima_posicao] = valor  # valor adicionado nessa última posição

    # percorre procurando a primeira ocorrência daquele valor, se encontrado retorna sua posição
    def procura(self, valor):
        for i in range(self.ultima_posicao + 1):
            if (self.array[i] == valor): return i

        print("Não existe esse valor")
        return -1

    # exclui um valor passado caso ele exista no vetor
    def exclue(self, valor):
        posicao = self.procura(valor)  # utiliza a função de busca para saber se há esse valor no array
        if posicao == -1:  # caso retorne -1 é pq não há
            print("Não existe esse valor")
            return
        else:
            for i in range(posicao, self.ultima_posicao + 1):   # looping que faz o seguinte: 1 7 8 4 2 4 -> 1 7 8 2 2 4
                self.array[i] = self.array[i + 1]               # -> 1 7 8 2 4 (4)  | o valor 4 foi removido, logo todos
                                                                # os valores após o 4 passaram uma casa à esquerda,
            self.ultima_posicao -= 1                            # sendo aquele último 4 apenas lixo residual
