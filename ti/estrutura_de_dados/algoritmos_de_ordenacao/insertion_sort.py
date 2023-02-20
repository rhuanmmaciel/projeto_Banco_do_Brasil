import numpy as np
import random

def insertion_sort(vetor):
    for i in range(1,len(vetor)):
        pos = i
        valor = vetor[i]
        for j in range(i - 1, -1, -1):
            if valor < vetor[j]:
                vetor[j + 1] = vetor[j]
                vetor[j] = valor
            else:
                j = -1
        print(f"{i}: {vetor}")


vetor = np.empty(10, dtype=int)

for i in range(len(vetor)):
    vetor[i] = random.random() * 50

print(f"Vetor inicial: {vetor}")
print()
insertion_sort(vetor)
print()
print(f"Vetor final: {vetor}")
