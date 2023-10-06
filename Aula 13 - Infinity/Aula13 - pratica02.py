# herança
class Conta:
    def __init__(self, num_conta, nome_cliente, saldo=0.0):
        self.numero = num_conta
        self.name = nome_cliente
        self.balance = saldo

    def exibirDados(self):
        print("\n-------Data-------\n")
        print(f"Conta: {self.numero}\n"
              f"Nome: {self.name}\n"
              f"Saldo: R$ {self.balance:.2f}\n")
        print("\n-------Data-------\n")

    def depositar(self, valor_deposito):
        if valor_deposito > 0:
            self.balance += valor_deposito
            print("\nDeposito Realizado!\n")
        else:
            print("\nValor Invalido!\n")


class ContaCorrente(Conta):
    def __init__(self, num_conta, nome_cliente, saldo, chequeespecial):
        super().__init__(num_conta, nome_cliente, saldo)
        self.cheque = chequeespecial
        self.saldo_mais_Cheque = self.balance + self.cheque

    def saque(self, valor):
        if self.saldo_mais_Cheque - valor >= 0:
            self.balance -= valor
        else:
            print("Saldo Insuficiente")

    def exibirDados(self):
        super().exibirDados()
        print(f"Saldo+Cheque: R$ {self.saldo_mais_Cheque:.2f}")


class ContaPoupa(Conta):
    def __init__(self, num_conta, nome_cliente, saldo, taxa_rendimento=0.1):
        super().__init__(num_conta, nome_cliente, saldo)
        self.taxa_de_rendimento = taxa_rendimento

    def saque(self, valor):
        if self.balance - valor >= 0:
            self.balance -= valor
        else:
            print("Saldo Insuficiente")

    def exibirDados(self):
        super().exibirDados()
        if self.balance > 0:
            self.balance += self.balance * self.taxa_de_rendimento
            print(f'\nSaldo após rendimento: {self.balance}\n')


clienteCorrente = ContaCorrente(int(input("\nconta do Cliente Corrente: ")), input("\nNome do Cliente Corrente: "),
                                float(input("\nSaldo Cliente Corrente: ")),
                                float(input("\nLimite Cheque Especial: ")))

clienteCorrente.depositar(float(input("\nValor do Deposito: ")))
clienteCorrente.saque(float(input("\nValor do Saque: ")))

clienteCorrente.exibirDados()

clientePoupa = ContaPoupa(int(input("\nconta do Cliente Poupança: ")), input("\nNome do Cliente Poupança: "),
                          float(input("\nSaldo do Cliente Poupança: ")))

clientePoupa.depositar(float(input("\nValor do Deposito: ")))
clientePoupa.saque(float(input("\nValor do Saque: ")))

clientePoupa.exibirDados()
