# Escreva uma função que recebe um parametro n, leia n números e retorne a quantidade de números perfeitos digitados
# Número perfeito = soma dos seus divisores é igual a ele mesmo

def numeroperfeito(n1):
    soma = 0
    for i in range(1, n1):
        if n1 % i == 0:
            soma += i
    return soma


def pergunta(n2):
    qtdper = 0
    for i in range(1, n2 + 1):
        n = int(input(f"Digite {i}º número: "))
        if numeroperfeito(n) == n:
            print("Perfeito")
            qtdper += 1
        else:
            print("Não é perfeito")
    print(f"Qtd. de Números perfeitos: {qtdper}")

n3 = int(input("Digite um número: "))

pergunta(n3)