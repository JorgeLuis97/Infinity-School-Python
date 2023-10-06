class Elevador:
    # Método construtor
    def __init__(self, andar_atual, qtd_pessoas,
                 qtd_andares, capacidade):
        self.andar_atual = andar_atual
        self.qtd_pessoas = qtd_pessoas
        self.qtd_andares = qtd_andares
        self.capacidade = capacidade

    # métodos
    def subir(self):
        if self.andar_atual < self.qtd_andares:
            self.andar_atual += 1
            print("Subindo...")
            print(f"Andar atual: {self.andar_atual}")
        else:
            print("Você está no ultimo andar!")

    def descer(self):
        if self.andar_atual > 0:
            self.andar_atual -= 1
            print("Descendo...")
            print(f"Andar atual: {self.andar_atual}")
        else:
            print("Você está no Térreo!")
    def entrar(self, qtd):
        if self.qtd_pessoas + qtd <= self.capacidade:
            self.qtd_pessoas += qtd
            print("Entrando...")
            print(f"Quantidade atual: {self.qtd_pessoas}")
        else:
            print("Capacidade não suporta essa quantidade!")
    def sair(self, qtd):
        self.qtd_pessoas -= qtd
        if self.qtd_pessoas < 0:
            self.qtd_pessoas = 0
        print("Saindo...")
        print(f"Quantidade atual: {self.qtd_pessoas}")

plaza = Elevador(5, 10, 7, 15)
plaza.subir()
plaza.subir()
plaza.subir()
plaza.entrar(5)
plaza.sair(15)
plaza.sair(2)

class Cachorro:
    def __init__(self, nome, raca, peso):
        self.name = nome
        self.race = raca
        self.weight = peso

    def comer(self):
        while self.weight != 25:
            self.weight += 1
        return f"Croc Croc Croc\n" \
               f"Agora ele pesa: {self.weight}Kg"


cachorro = Cachorro("Bento", "Terrier", 8)
cachorro2 = Cachorro("Jin", "Husky", 12)
print(f"\nO cachorro {cachorro.name} da raça {cachorro.race} pesa {cachorro.weight}kg e come: {cachorro.comer()}\n")
print(f"\nO cachorro {cachorro2.name} da raça {cachorro2.race} pesa {cachorro2.weight}kg e come: {cachorro2.comer()}\n")
