def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n-1)


def potencia(base, expoente):
    if expoente == 0:
        return 1
    expoente -= 1

    return base * potencia(base, expoente)


print(potencia(2, 10))
print(fatorial(6))
