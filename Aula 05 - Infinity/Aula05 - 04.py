# Escreva uma função que recebe um parametro n, leia n números e imprima a soma destes números

n = int(input("Digite um número: "))

def somar(n1):
    soma = 0
    for i in range(1, n1 + 1):
        soma += i
        print(soma)
    print(f"Soma é {soma}")



somar(n)
