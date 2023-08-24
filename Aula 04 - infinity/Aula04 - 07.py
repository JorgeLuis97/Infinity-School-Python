# 7. Escreva uma função que recebe um número por parametro e imprima todos os números pares de 0 até este número

numero = int(input("Digite um número: "))


def seq_numero_par(n1):
    for i in range(0, n1+1):
        if i % 2 == 0:
            print(i)


seq_numero_par(numero)
