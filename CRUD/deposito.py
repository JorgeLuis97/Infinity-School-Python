from banco import obterconta


def depositar(conta: int, valor: float) -> None:
    cliente = obterconta(conta)
    if cliente:
        cliente['saldo'] = cliente['saldo'] + valor
        print("Deposito realizado com sucesso!")
    else:
        print("Cliente não existe!")
