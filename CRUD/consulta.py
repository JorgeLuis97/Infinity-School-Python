from banco import obterconta


def consultarsaldo(conta: int) -> None:
    cliente = obterconta(conta)
    if cliente:
        print(f"Saldo: R$ {cliente['saldo']}")
    else:
        print("Cliente não existe!")
