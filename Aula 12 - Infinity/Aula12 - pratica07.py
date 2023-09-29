class Elevador:
    def __init__(self, ultimo_andar: int, andar_atual=0):
        self.ultimo = ultimo_andar
        self.atual = andar_atual

    def subir(self, destino):
        if destino > self.ultimo:
            print("Andar Invalido")
        else:
            self.atual = destino
            print(f'Andar Atual: {self.atual}')

    def descer(self, destino):
        if destino < 0:
            print("Andar Invalido")
        else:
            self.atual = destino
            print(f'Andar Atual: {self.atual}')


while True:
    passageiro = Elevador(13, int(input(f"Qual Andar deseja ir: ")))

    if passageiro.atual == -1:
        print("\nSaindo do elevador...\n")
        break
