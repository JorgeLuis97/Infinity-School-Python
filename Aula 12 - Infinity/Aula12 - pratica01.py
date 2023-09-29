class Conta:
    def __init__(self, numero_conta: int, nome_cliente: str, saldo_cliente=0) -> None:
        self.conta = numero_conta
        self.cliente = nome_cliente
        self.saldo = float(saldo_cliente)


cliente = Conta(int(input("conta do Cliente: ")), input("Nome do Cliente: "), int(input("Saldo do Cliente: ")))

print("\n------- Informações -------\n")
print(f'Nome: {cliente.cliente}\n'
      f'Numero da Conta: {cliente.conta}\n'
      f'Saldo: {cliente.saldo}\n')
print("---------------------------\n")
