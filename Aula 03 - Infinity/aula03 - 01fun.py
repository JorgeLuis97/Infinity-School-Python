def dois_numeros():
    soma = 0
    for i in range(1, 3):
        n = int(input(f"Digite {i}º número: "))
        soma += n

    print(f"A soma pe {soma}")


dois_numeros()
