# 1. Escreva uma função que recebe um número e imprima a tabuada de multiplicação
# deste número

n = int(input("Digite um número: "))

def tabuada(n1):
    for i in range(1, 10 + 1):
        resultado = i * n1
        print(f"{i} x {n1} = {resultado}")

tabuada(n)
