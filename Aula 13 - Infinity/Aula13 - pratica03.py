# 1. Crie uma classe chamada Eletronico com os atributos
# - ligado = False
# - Voltagem
# e crie um método para ligar e desligar o Eletronico
# 2. Crie uma classe chamada Televisao que herda de Eletronico com os atributos
# - volume max
# - volume atual
# - qtd_canais
# - canal_atual (1, 2, 3, 4, 5... qtd_canais)
# Crie métodos para aumentar e diminuir o volume e para mudar de canal
#
# 3. Crie uma classe chamada Ventilador que herda de Eletronico com os atributos
# - velocidades (1, 2, 3)
# Crie um método para alterar a velocidade do ventilador

class Eletronico:
    def __init__(self, ligado=False, voltagem):
        self.power = ligado
        self.volts = voltagem

    def Ligar(self):
        if not self.power:
            self.power = True
        else:
            print("Já se encontra Ligado")

    def Desligar(self):
        if self.power:
            self.power = False
        else:
            print("Já se encontra Desligado")

class Televisao(Eletronico):
    def __init__(self, ligado, voltagem, volume_max, volume_atual, qtd_canais, canal_atual):
        super().__init__(ligado, voltagem)
        self.soundmax = volume_max
        self.soundactual = volume_atual
        self.channels = qtd_canais
        self.actualchannel = canal_atual

    def aumentarvolume(self, valor):
        if self.power == True:
            if self.soundactual + valor >= self.soundmax: