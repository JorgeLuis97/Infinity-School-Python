def compa():
    n1 = float(input("Digite o primeiro numero: "))
    n2 = float(input("digite o segundo numero: "))

    if n1 > n2:
        print(f"{n1} é maior que {n2}")
    elif n2 > n1:
        print(f"{n2} é maior que {n1}")
    else:
        print('Numeros iguais')

compa()
