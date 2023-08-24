# 5. Escreva uma função que recebe dois números por parametro e imprima o maior

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))


def maior_menor(n1, n2):
    if n1 > n2:
        print(f"{n1} é maior")
    elif n2 > n1:
        print(f"{n2} é maior")
    else:
        print("Os dois números são iguais")


maior_menor(numero1, numero2)
