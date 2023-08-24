# 4. Escreva uma função que recebe um número por parametro e informe se ele este parametro é par ou ímpar

numero1 = int(input("Digite um número: "))


def impar_ou_par(n1):
    if n1 % 2 == 0:
        print(f"{n1} é Par")
    else:
        print(f"{n1} é Impar")


impar_ou_par(numero1)
