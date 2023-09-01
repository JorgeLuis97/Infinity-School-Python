from banco import obterconta


def saque(conta: int, valor: float) -> None:
    cliente = obterconta(conta)
    if cliente:
        if cliente['saldo'] >= valor:
            cliente['saldo'] = cliente['saldo'] - valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo Insuficiente")
    else:
        print("Cliente não existe!")
