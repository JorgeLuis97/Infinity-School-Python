class Elevador:
    def __init__(self, ultimo_andar: int, andar_destino: int, andar_atual=0):
        self.ultimo = ultimo_andar
        self.atual = andar_atual
        self.destino = andar_destino
        # self.pessoas = qtd_pessoas
        # self.cap = capacidade

    def subir(self, destino):
        if destino > self.ultimo:
            print("Andar Invalido")

        elif destino < self.atual and destino < self.ultimo:
            while self.atual != destino:
                self.atual += 1
                print(f'Andar Atual: {self.atual}')

    def descer(self, destino):
        if destino < 0 or destino < self.atual:
            print("Andar Invalido")
        else:
            while self.atual != destino:
                self.atual -= 1
                print(f'Andar Atual: {self.atual}')

    def entrar(self):
        pass

andar_atual = 0

while True:
    passageiro = Elevador(13, int(input(f"Qual Andar deseja ir: ")), andar_atual)

    if passageiro.atual == -1:
        print("\nSaindo do elevador...\n")
        break

    elif passageiro.atual > passageiro.destino:
        passageiro.descer(passageiro.destino)

    elif passageiro.atual < passageiro.destino:
        passageiro.subir(passageiro.destino)
