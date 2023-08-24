def qtdpar():
    par = 0
    impar = 0
    maiorque20 = 0
    for i in range(1, 11):
        n = int(input(f"{i}. Digite um número: "))
        if n % 2 == 0:
            print(f"O número {n} é PAR")
            par += 1
        else:
            print(f"O número {n} é IMPAR")
            impar += 1
        if n > 20:
            maiorque20 += 1
    print(f"Quantidade de número pares: {par}")
    print(f"Quantidade de número impares: {impar}")
    print(f"Quantidade de número maior que 20: {maiorque20}")


qtdpar()
