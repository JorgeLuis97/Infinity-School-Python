class Conta:
    def __init__(self, numero_conta: int, nome_cliente: str, chequeespecial=0.0, saldo_cliente=0.0) -> None:
        self.conta = numero_conta
        self.cliente = nome_cliente
        self.saldo = saldo_cliente
        self.chequeespecial_limite = chequeespecial
        self.saldo_mais_Cheque = self.saldo + self.chequeespecial_limite
        self.taxa_de_rendimento = 0.01

    def depositar(self, valor_deposito):
        if valor_deposito > 0:
            self.saldo += valor_deposito
            print("\nDeposito Realizado!\n")
        else:
            print("\nValor Invalido!\n")

    def saque(self, valor):
        if self.saldo_mais_Cheque - valor >= 0:
            self.saldo -= valor
        else:
            print("Saldo Insuficiente")


cliente = Conta(int(input("conta do Cliente: ")), input("Nome do Cliente: "),
                float(input("Limite Cheque Especial: ")), float(input("Saldo do Cliente: ")))
cliente.depositar(float(input("Valor do Deposito: ")))
cliente.saque(float(input("Valor do Saque: ")))
cliente.rendimento()

print("\n------- Informações -------\n")
print(f'Nome: {cliente.cliente}\n'
      f'Numero da Conta: {cliente.conta}\n'
      f'Saldo: R$ {cliente.saldo:.2f}\n'
      f'Saldo+Limite: R$ {cliente.saldo_mais_Cheque:.2f}')
print("---------------------------\n")
