print("-----------------------\n")
print("Pedra = 1\n"
      "Papel = 2\n"
      "Tesoura = 3\n")
print("-----------------------\n")
a = int(input("Jogador 1 qual sua Jogada: "))
print("-----------------------\n")
print("Pedra = 1\n"
      "Papel = 2\n"
      "Tesoura = 3\n")
print("-----------------------\n")
b = int(input("Jogador 2 qual sua Jogada: "))

if a == 1 and b == 3:
    print("Pedra vence tesoura então Jogador 1 venceu!")
elif a == 2 and b == 1:
    print("Papel vence Pedra então Jogador 1 venceu!")
elif a == 3 and b == 2:
    print("Tesoura vence Papel então Jogador 1 venceu!")
elif b == 1 and a == 3:
    print("Pedra vence Tesoura então Jogador 2 venceu!")
elif b == 2 and a == 1:
    print("Papel vence Pedra então Jogador 2 venceu!")
elif b == 3 and a == 2:
    print("Tesoura vence Papel então Jogador 2 venceu!")
else:
    print("!!Valor Invalido!!")