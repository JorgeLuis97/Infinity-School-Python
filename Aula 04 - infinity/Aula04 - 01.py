# 1. Escreva uma função que recebe um parametro lado, em seguida calcule a área do quadrado e exiba o resultado na tela
# area = lado * lado

numero1 = int(input("Digite o primeiro número: "))


def area(n1):
    return n1 * n1


soma = area(numero1)

print(f"A area é {soma}")
