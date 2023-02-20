import numpy as np
import random


def selection_sort(vetor):

    for i in range(len(vetor)):

        min = vetor[i]
        min_pos = i
        for j in range(i+1, len(vetor)):

            if vetor[j] < min:
                min = vetor[j]
                min_pos = j

        vetor[min_pos] = vetor[i]
        vetor[i] = min
        print(f"{i + 1}º = {vetor}")


vetor = np.empty(10, dtype=int)

for i in range(len(vetor)):
    vetor[i] = random.random() * 50

print(vetor)
selection_sort(vetor)
print(vetor)
