#  Número perfeito:
# O número perfeito é resultado da soma de todos os seus divisores menos ele proprio
# Ex: 6 é um número perfeito pois a soma de seus divisores (1, 2, 3) é igual a 6.
# Escreva uma função que recebe um número e informe se ele é ou não um número perfeito

numero = int(input("Digite um número: "))


def numero_perfeito(n1):
    soma = 0
    for i in range(1, n1):
        if n1 % i == 0:
            soma += i
    return soma


perfeito = numero_perfeito(numero)

if perfeito == numero:
    print("Número perfeito")
else:
    print("Não perfeito")
