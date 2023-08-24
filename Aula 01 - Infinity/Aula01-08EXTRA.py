valor = 0
lista = []
for i in range(1, 3):
    listateste = []
    nome = input(f"Nome do {i}º Jogador: ")
    listateste.append(nome)
    jogada = input("Impar ou Par: ").upper()
    listateste.append(jogada)
    valor = int(input("Número: "))
    listateste.append(valor)
    lista.append(listateste)

segundos_elementos = [sublista[2] for sublista in lista]
soma = sum(segundos_elementos)

print(lista)

if soma % 2 == 0:
    vencedor = lista[0][0] if lista[0][1] == 'PAR' else lista[1][0]
else:
    vencedor = lista[1][0] if lista[0][1] == 'PAR' else lista[0][0]

print(f"O vencedor é: {vencedor}")
