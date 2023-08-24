# 6. Escreva uma função que recebe um número por parametro e imprima uma sequencia de 0 até este número

numero = int(input("Digite um número: "))

def seq_numero(n1):
    for i in range(0, n1+1):
        print(i)


seq_numero(numero)
