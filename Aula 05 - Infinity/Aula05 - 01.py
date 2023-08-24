# 1. Escreva uma função que recebe tempo da viagem em horas e a velocidade média em km por
# parametros. Em seguida calcule o consumo de combustivel desse veiculo, sabendo que o veiculo faz 12km/L.
# E retorne o valor do consumo desta viagem. Em seguida imprima o resultado na tela

def distancia(tempo, velocidade):
    return tempo * velocidade


tempo1 = int(input('Digite o tempo da viagem: '))
velocidade1 = int(input('Digite a velocidade média do veiculo: '))


distancia2 = distancia(tempo1, velocidade1)


def consumo(distancia):
    return distancia / 12


consumo2 = consumo(distancia2)

print(f"Consumo total: {consumo2:.2f}")
