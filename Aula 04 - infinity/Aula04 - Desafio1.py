# D-1 Escreva uma função que recebe um número por parametro e imprima se ele é ou não um número primo

numero = int(input("Digite um número: "))


def numero_primo(n1):
    eprimo = 0
    for i in range(1, n1 + 1):
        if n1 % i == 0:
            eprimo += 1
    if eprimo == 2:
        print("Número Primo")
    else:
        print("Não é primo")


numero_primo(numero)
