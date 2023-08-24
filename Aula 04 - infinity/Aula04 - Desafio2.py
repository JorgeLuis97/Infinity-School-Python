# D-2. Escreva uma função que recebe um número por parametro e
# imprima a soma de todos os números pares de 0 até este número

numero = int(input("Digite um número: "))


def numero_par(n1):
    somapar = 0
    for i in range(1, n1 + 1):
        if i % 2 == 0:
            print(i)
            somapar += i
    print(f"A soma é {somapar}")


numero_par(numero)
