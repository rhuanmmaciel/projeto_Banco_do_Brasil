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
        self.__topo -= 1  # o topo retrocede numa posição quando um item é desempilhado
        return self.__valores[self.__topo + 1]  # o valor é retornado caso queira utilizá-lo


def verifica(expressao):  # função que verifica se a expressão é válida ou não
    for i in expressao:  # percorre todos os caracteres da variável expressão
        if i == '{' or i == '[' or i == '(':  # caso encontre um (, [ ou { será empilhado
            pilha.empilhar(i)

        if i == '}' or i == ')' or i == ']':  # caso encontre um ), ] ou }, deverá ser verificado
                                              # se a expressão está correta
            topo = pilha.desempilhar()  # o último item da pilha é desempilhado
            if not topo:  # caso topo seja falso, é porque a pilha está vazia, e logo a expressão está incorreta
                return False
            if (i == ')' and (topo == '[' or topo == '{')) or \
                    (i == ']' and (topo == '(' or topo == '{')) or \
                    (i == '}' and (topo == '[' or topo == '(')):  # caso o item desempilhado e o atual caracter
                                                                  # i não sejam um par, então a expressao está incorreta
                return False

    return pilha.desempilhar() == False  # caso a função, após percorrido o for, não tenha retornado falso, é porque
                                         # não foram encontrados problemas, entretanto ainda pode acontecer de
                                         # existirem elementos na pilha, o que significaria que a expressão está
                                         # incorreta por falta de elementos, por exemplo: (a+b) - [4+5
                                         # Essa expressão não possui nenhum item incorreto, porém o último colchete
                                         # não foi fechado, logo quando desempilhar o valor retornado será [, e não
                                         # o valor booleano False


pilha = Pilha(100)  # teste

equacao = input("Digite uma expressão com () [] e {}")

print(verifica(equacao))
