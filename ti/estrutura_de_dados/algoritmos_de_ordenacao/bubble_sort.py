import numpy as np
import random


def bubble_sort(vetor):
    n = len(vetor)
    ultima_pos = n

    k = 1

    while ultima_pos != 0:
        for i in range(n - 1):
            valor = vetor[i]
            if vetor[i] > vetor[i+1]:
                aux = vetor[i]
                vetor[i] = vetor[i+1]
                vetor[i+1] = aux

        ultima_pos -= 1
        print(f"{k}º = {vetor}")
        k += 1


vetor = np.empty(10, dtype=int)

for i in range(len(vetor)):
    vetor[i] = random.random() * 50

print(vetor)
bubble_sort(vetor)
print(vetor)
