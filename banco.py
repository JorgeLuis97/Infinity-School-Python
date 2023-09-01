banco = [
    {'conta': 1, 'nome': 'Mariana', 'saldo': 159.99},
    {'conta': 2, 'nome': 'Jonas', 'saldo': 259.99}
]

conta_atual = 2


def adicionarconta(nome: str, saldo: float) -> None:
    global conta_atual
    conta_atual += 1

    cliente = {
        "conta": conta_atual,
        "nome": nome,
        "saldo": saldo
    }
    banco.append(cliente)
    print("Cliente cadastrado com Sucesso!")


def obterconta(conta: int) -> dict or None:
    for cliente in banco:
        if cliente['conta'] == conta:
            return cliente
    return None


def deletarconta(conta: int) -> None:
    cliente = obterconta(conta)
    if cliente:
        banco.remove(cliente)
        print("Cliente deletado com sucesso!")
    else:
        print("Cliente não existe!")


def editarnome(novo_nome: str, conta: int) -> None:
    cliente = obterconta(conta)
    if cliente:
        cliente['nome'] = novo_nome
        print("Nome alterado com sucesso!")
    else:
        print("Cliente não exite!")


def consultarcliente(conta: int) -> None:
    cliente = obterconta(conta)
    if cliente:
        print(f"N. conta: {conta}\n"
              f"Cliente: {cliente['nome']}\n"
              f"Saldo: R$ {cliente['saldo']:.2f}\n")
    else:
        print("Cliente não encontrado!")


def listarcontas() -> None:
    for cliente in banco:
        consultarcliente(cliente['conta'])
        print("-------------------------")
