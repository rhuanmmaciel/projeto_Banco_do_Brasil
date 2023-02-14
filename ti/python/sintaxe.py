#!/usr/bin/env python
# coding: utf-8

# Exercício 1:

# In[ ]:


n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

print(f"A soma de {n1} + {n2} é {n1 + n2}")
print(f"A subtração de {n1} - {n2} é {n1 - n2}")
print(f"A multiplicação de {n1} * {n2} é {n1 * n2}")
print(f"A divisão de {n1} / {n2} é {n1 / n2}")


# Exercício 2:

# In[6]:


tempo = float(input("Digite o tempo em horas: "))
velocidade_media = float(input("Digite a velocidade média em km/h"))

distancia = tempo * velocidade_media
litros = distancia / 12

print(" Velocidade média:", velocidade_media, "\n", 
      "Tempo:", tempo, "\n",
      "Distância:", distancia, "\n",
      "Litros:", litros)


# Exercício 3: If's

# In[7]:


idade = int(input("Digite a sua idade: "))

if(idade >= 0 and idade <= 12): 
    print("Criança")
elif(idade >= 13 and idade <= 17):
    print("Adolescente")
elif(idade >= 18):
    print("Adulto")
else:
    print("Inválido")


# Exercício 4: If's

# In[19]:


media = (float(input("Nota 1: ")) + float(input("Nota 2: ")) + float(input("Nota 3: "))) / 3

exame = 1 if media > 4 and media <= 6 else 0 if media >= 0 and media <= 4 else 2

if(exame == 0):
    print("Reprovado")
elif(exame == 2):
    print("Passou")
else:
    nota_exame = float(input("Nota exame"))
    if(nota_exame > 6):
        print("Passou")
    else:
        print("Reprovado")


# Exercício 5: For

# In[25]:


soma = 0

for i in range(1, 6):
    soma += float(input(f"Digite a nota {i}"))
   
print(soma / i)


# Exercício 6: For

# In[29]:


for i in range(1, 11):
    print(i * 3)


# Exercício 7: Listas

# In[8]:


lista = []
for i in range(0, 5):
    lista.append(int(input("Digite um número inteiro")))
    
sum = 0
for i in lista:
    sum += i   
    
print(sum)    


# Exercício 8: Dicionários

# In[20]:


dic = {}
for i in range(0, 3):
    dic.update({input("Digite o nome: "): float(input("Digite a nota: "))})
    
sum = 0    
for i in dic.values():
    sum += i
    
print(sum / len(dic))    


# Exercício 9: Matriz

# In[76]:


import numpy as np

matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])

sum = 0
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        sum += matriz[i][j]
    
print(sum)    


# Exercício 10: Função

# In[80]:


def converte_fahrenheit():
    return (float(input("Digite a temperatura em graus celsius: ")) * 9 + 160) / 5

def converte_fahrenheit_2(c):
    return (c * 9 + 160) / 5

def printa(c):
    print(c)
    
printa(converte_fahrenheit())
printa(converte_fahrenheit_2(0))


# Exercício 11: Função

# In[97]:


def leitura():
    return (int(input("Digite o tempo: ")), float(input("Digite a velocidade média utilizada: ")))

def distancia(x):
    return x[0] * x[1]

def litros(x):
    return x / 12

dados = leitura()
print(f"Velocidade média: {dados[0]}\nTempo gasto: {dados[1]}\nDistância: {distancia(dados)}\nLitros: {litros(distancia(dados))}")


# Exercício 12: Orientação a objeto

# In[11]:


class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
    def media(self):    
        return (self.nota1 + self.nota2) / 2
    def dados(self):
        return (self.nome, self.nota1, self.nota2)
    def resultado(self):
        return "Aprovado" if self.media() >= 6 else "Reprovado" 
    
aluno1 = Aluno("Rhuan", 10, 10)
aluno2 = Aluno("Douglas", 8, 3.5)

print(f"O aluno {aluno2.dados()[0]} está {aluno2.resultado()} com média {aluno2.media()}")
print(f"Enquanto o aluno {aluno1.dados()[0]} está {aluno1.resultado()} com média {aluno1.media()}")

