# Escreva uma função em Python que recebe uma lista de números inteiros e retorna a média aritmética dos valores.
numeros = [5, 10, 15, 20]


def media():
    soma = 0
    for i in numeros:
        soma += i
    return soma / len(numeros)


Media = media()

print(f"Media: {Media}")
