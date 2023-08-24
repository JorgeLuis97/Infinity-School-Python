# Escreva uma função que recebe uma parametro n, leia n números e imprima o maior e o menor no final
n1 = int(input("Digite a quantidade de perguntas: "))


def somar(n1):
    lista = []
    for i in range(1, n1 + 1):
        n = int(input("Digite um número: "))
        lista.append(n)

    maior = max(lista)
    menor = min(lista)
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")


somar(n1)
