# Escreva uma função que recebe um parametro n, leia n números e imprima a média destes números

n = int(input("Digite um número: "))

def somar(n1):
    soma = 0
    for i in range(1, n1 + 1):
        soma += i
        print(soma)
    media = soma / n1
    print(f"Media é {media}")



somar(n)
