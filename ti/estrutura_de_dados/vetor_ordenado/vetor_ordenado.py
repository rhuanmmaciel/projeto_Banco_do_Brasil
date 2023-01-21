import numpy as np
import random as rd

class Vetor:
    def __init__(self, capacidade):                  # ao criar o vetor a sua capacidade máxima deve ser informada
        self.capacidade = capacidade                 # pois aloca memória estaticamente
        self.ultima_posicao = -1
        self.array = np.empty(capacidade, dtype=int)

    def imprime(self): # a impressão funciona percorrendo todo array caso ele não seja nulo
        print("------------")
        if self.ultima_posicao >= 0:
            for i in range(self.ultima_posicao + 1):
                print(str(i) + " - " + str(self.array[i]))
        else:
            print("Vetor vazio")
        print("------------")

    def insere(self, valor):
        if self.ultima_posicao + 1 >= self.capacidade: # verifica se o vetor não está cheio
            print("Vetor cheio")
            return # caso esteja ele sairá da função sem inserir
        for posicao_correta in range(self.ultima_posicao + 1): # for que percorre todo tamanho do array

            if valor < self.array[posicao_correta]: # esse for acima irá repetir até encontrar a primeira posição que
                                                    # possua um número maior que o valor inserido, quando encontrado
                                                    # esse if será acionado

                for posicao_i in range(self.ultima_posicao + 1, posicao_correta, -1): # esse for irá começar da última
                                                                                      # posição e irá até a posição que
                                                                                      # foi encontrado o primeiro valor
                                                                                      # maior que o que será inserido
                    self.array[posicao_i] = self.array[posicao_i - 1] # essa instrução passará cada valor para a direita

                self.array[posicao_correta] = valor # depois de todos os números serem realocados uma posição a direita,
                                                    # será possível colocar o valor inserido na sua posição correta sem
                                                    # perder nenhum dado
                self.ultima_posicao += 1
                return

        self.array[self.ultima_posicao + 1] = valor # esse trecho de código será lido apenas quando o for percorrer todo
                                                    # vetor e não encontrar nenhum valor maior que o que será inserido,
                                                    # portanto basta apenas inserí-lo na última posição
        self.ultima_posicao += 1

    def pesquisa(self, valor):
        if self.ultima_posicao < 0: # verificação de vetor nulo
            print("Vetor Vazio")
            return -1
        for i in range(self.ultima_posicao + 1): # for que irá percorrer todo vetor
            if valor == self.array[i]: # caso encontre
                print(f"Valor encontrado na posição {i}")
                return i
            if valor > self.array[i]: # caso o valor pesquisado já seja maior que o valor dessa posição, e, no entanto,
                                      # não foi encontrado ainda, dessa forma conclui-se que esse valor pesquisado não
                                      # está nesse array
                i = self.ultima_posicao + 1 # o i se tornará o seu limite superior, logo o for não se repetirá mais
        print("Valor não encontrado")
        return -1

    def excluir(self, valor): # a exclusão se dá da mesma forma que o vetor não ordenado
        posicao = self.pesquisa(valor)
        if posicao < 0:
            return
        for i in range(posicao, self.ultima_posicao):
            self.array[i] = self.array[i + 1]

        self.ultima_posicao -= 1

    def pesquisa_binaria(self, valor):
        if self.ultima_posicao < 0: # verificação de vetor nulo
            print("Vetor vazio")
            return -1

        repeticoes_necessarias = 1
        min = 0 # seta o valor mínimo como o inicial
        max = self.ultima_posicao # seta o valor máximo como o último do array
        acabou_array = False # variável que indica se todo o vetor já foi verificado
        while not acabou_array:
            metade = int((min+max) / 2) # pega o valor que está no ponto médio entre o mínimo e o máximo
            if valor == self.array[metade]: # verifica se o valor pesquisado é igual a esse ponto médio
                print(f"Encontrado na posição {metade}, foram necessárias {repeticoes_necessarias} repetições")
                return metade
            if valor > self.array[metade]: # verifica se o valor pesquisado é maior do que o ponto médio
                min = metade # se é maior então o limite mínimo deve ser o ponto médio
            if valor < self.array[metade]: # verifica se é menor
                max = metade # se é menor então o limite máximo deve ser o ponto médio
            if (max - min == 1 or max - min == 0): # caso a diferença entre o limite mínimo e o máximo seja 0 ou 1,
                                                   # estamos chegando no final da pesquisa, e deve-se verificar se
                                                   # o número pesquisado é algum dos dois remanescentes, pois caso
                                                   # essa condição seja verdade, ou estamos nesse caso [x, x] ou
                                                   # [x, x+1]

                if valor == self.array[min] or valor == self.array[max]: # verifica se o valor pesquisado é um dos
                                                                         # limites inferior ou superior

                    print(f"Encontrado na posição {min if valor == self.array[min] else max}, foram necessárias {repeticoes_necessarias} repetições")
                    return min if valor == self.array[min] else max # caso tenha entrado nesse if, é porque encontramos
                                                                    # o valor, resta saber se é o limite mínimo ou o
                                                                    # máximo, retornando quem quer que seja

                acabou_array = True # e se caso chegamos ao final da pesquisa binária e o valor pesquisado não está
                                    # nem na posição máxima e nem na mínima, então esse valor não está no vetor, logo
                                    # a nossa variável de controle assume o valor que quebra o while
            repeticoes_necessarias += 1

        print("Não existe esse valor no vetor") # chegando aqui sabemos que não há esse número no array
        return -1

v = Vetor(500)
v.insere(2849) # inserido um valor específico para fazer o teste
for i in range(499):
    v.insere(rd.random() * 20000) # inserção de 499 números aleatórios entre 0 e 20000

v.imprime()
v.pesquisa_binaria(2849) # pesquisa binária desse valor específico
