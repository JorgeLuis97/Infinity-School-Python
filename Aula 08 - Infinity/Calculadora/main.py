from operacoes import soma as som, divisao as div, multiplicacao as mult, subtracao as sub

while True:
    print('-----Números-----\n')
    n1 = float(input("Primeiro número: "))
    n2 = float(input("Segundo número: "))
    print('-----Números-----\n')

    opcao = int(input("1 - Soma\n"
                      "2 - Divisão\n"
                      "3 - Multiplicação\n"
                      "4 - Subtração\n"
                      "5 - Sair\n"
                      "------------------\n"
                      "Selecione o número da Opção: "))
    print("")
    if opcao == 1:
        print("-----Resultado-----")
        print(f"{n1} + {n2} = {som.somar(n1, n2)}")
        print("-------------------\n")
    elif opcao == 2:
        print("-----Resultado-----")
        print(f"{n1} / {n2} = {div.dividir(n1, n2):.2f}")
        print("-------------------\n")
    elif opcao == 3:
        print("-----Resultado-----")
        print(f"{n1} * {n2} = {mult.multiplicar(n1, n2):.2f}")
        print("-------------------")
    elif opcao == 4:
        print("-----Resultado-----")
        print(f"{n1} - {n2} = {sub.subtrair(n1, n2):.2f}")
        print("-------------------\n")
    elif opcao == 5:
        print("Saindo ...")
        break
    else:
        print("!!Opção invalida!!")
