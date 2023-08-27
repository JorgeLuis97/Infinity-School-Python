# b)Escreva um trecho de código que use a função random para gerar um número inteiro aleatório entre 10 e 20 (inclusive)
import random

x = random.randint(10, 20)

print(x)

# c) Escreva um trecho de código que use a função random
# para gerar uma lista com 5 elementos inteiros aleatórios entre 1 e 100 (inclusive).
lista = []
for i in range(1, 6):
    x = random.randint(1, 100)
    lista.append(x)

print(lista)
