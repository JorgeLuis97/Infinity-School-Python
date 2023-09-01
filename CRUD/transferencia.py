from banco import obterconta


def transferencia(conta1: int, valor: float, conta2: int) -> None:
    cliente = obterconta(conta1)
    destino = obterconta(conta2)
    if cliente:
        if cliente['saldo'] >= valor:
            cliente['saldo'] = cliente['saldo'] - valor
            destino['saldo'] = destino['saldo'] + valor
            print("Transferencia Realizada com sucesso!")
        else:
            print("Saldo insuficiente!")
    else:
        print("Cliente não existe!")



