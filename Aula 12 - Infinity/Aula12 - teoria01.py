# como criar classe
class Carro:
    # Metodo construtor
    # Metodo que é executado quando o OBJ é criado
    def __init__(self, model: str, co: str, marc: str, an: int) -> None:
        # Atributos e metodos
        # Atributos = Caracteristicas\Variaveis
        # Metodos = Ações/comportamentos/funções
        self.marca = marc
        self.modelo = model
        self.cor = co
        self.ano = an
        self.velocidade_atual = 0
        print(f"{self.modelo} {self.cor} da {self.marca} Ano:{self.ano} acaba de ser Criado")

    def exibirInformacoes(self):
        print("\n---- informações do veiculo ----\n")
        print(f"Marca: {self.marca}\n"
              f"Modelo: {self.modelo}\n"
              f"Ano: {self.ano}\n"
              f"Velocidade: {self.velocidade_atual} Km/h\n")
        print("\n---- informações do veiculo ----\n")

    def acelerar(self, velocidade):
        self.velocidade_atual += velocidade



carro1 = Carro("Uno", "Azul", "Fiat", 2023)
carro2 = Carro("Argo", "Vermelho", "Fiat", 2022)
carro3 = Carro("Mobi", "Preto", "Fiat", 2021)
velocidade = 0
while True:
    velocidade += 1
    if velocidade < 516051605165106:
        carro1.acelerar(velocidade)
        carro1.exibirInformacoes()
    else:
        break
