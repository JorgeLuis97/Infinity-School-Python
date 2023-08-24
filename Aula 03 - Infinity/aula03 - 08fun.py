def viagem():
    km = float(input("Quantos KM: "))
    horas = float(input("Quantas Horas de viagem: "))

    comprimento = km * horas

    consumo = comprimento / 10

    print(consumo)


viagem()
