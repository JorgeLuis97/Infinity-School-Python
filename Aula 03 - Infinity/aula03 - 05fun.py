def medias():
    n1 = float(input("Digite a 1º nota: "))
    n2 = float(input("Digite a 2º nota: "))
    n3 = float(input("Digite a 3º nota:"))

    media = (n1 + n2 + n3) / 3

    if media >= 6:
        print("Aprovado")
    else:
        print("Não aprovado")

    print(f"A média é {media:.2f}")


medias()
