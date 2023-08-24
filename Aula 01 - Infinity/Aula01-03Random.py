import random

vitoria = False

while not vitoria:
    print("-----------------------\n")
    print("Pedra = 1\n"
          "Papel = 2\n"
          "Tesoura = 3\n")
    print("-----------------------\n")
    b = random.randint(1, 3)
    a = int(input("Jogador 1 qual sua Jogada: "))
    if a == 1 and b == 3:
        print("-----------------------------------------\n")
        print("Pedra vence tesoura então Jogador 1 venceu!\n")
        print("-----------------------------------------\n")
        vitoria = True
    elif a == 2 and b == 1:
        print("-----------------------------------------\n")
        print("Papel vence Pedra então Jogador 1 venceu!\n")
        print("-----------------------------------------\n")
        vitoria = True
    elif a == 3 and b == 2:
        print("-----------------------------------------\n")
        print("Tesoura vence Papel então Jogador 1 venceu!\n")
        print("-----------------------------------------\n")
        vitoria = True
    elif b == 1 and a == 3:
        print("----------------------------------\n")
        print("Pedra vence Tesoura então AI venceu!\n")
        print("----------------------------------\n")
    elif b == 2 and a == 1:
        print("----------------------------------\n")
        print("Papel vence Pedra então AI venceu!\n")
        print("----------------------------------\n")
    elif b == 3 and a == 2:
        print("----------------------------------\n")
        print("Tesoura vence Papel então AI venceu!\n")
        print("----------------------------------\n")
    elif a == b:
        print("----------------------------------\n")
        print("           !!EMPATE!!               ")
        print("----------------------------------\n")
    else:
        print("----------------------------------\n")
        print("           VALOR INVALIDO           ")
        print("----------------------------------\n")
