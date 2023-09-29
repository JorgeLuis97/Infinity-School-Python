class Conta:
    def __init__(self, numero_conta: int, nome_cliente: str, saldo_cliente=0.0) -> None:
        self.conta = numero_conta
        self.cliente = nome_cliente
        self.saldo = saldo_cliente

    def depositar(self, valor_deposito):
        if valor_deposito > 0:
            self.saldo += valor_deposito
            print("\nDeposito Realizado!\n")
        else:
            print("\nValor Invalido!\n")


cliente = Conta(int(input("conta do Cliente: ")), input("Nome do Cliente: "), float(input("Saldo do Cliente: ")))
cliente.depositar(float(input("Valor do Deposito: ")))


print("\n------- Informações -------\n")
print(f'Nome: {cliente.cliente}\n'
      f'Numero da Conta: {cliente.conta}\n'
      f'Saldo: R$ {cliente.saldo:.2f}\n')
print("---------------------------\n")
