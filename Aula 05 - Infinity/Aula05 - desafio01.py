# 3. Escreva uma função que recebe um número n por parametro.
# Em seguida leia n números e ao final retorne a quantidade de números primos digitados
def numero_primo(n1):
    eprimo = 0
    for i in range(1, n1 + 1):
        if n1 % i == 0:
            eprimo += 1
    return eprimo


def pergunta(n2):
    soma = 0
    for i in range(1, n2 + 1):
        pergunta1 = int(input("Qual o número: "))
        if numero_primo(pergunta1) == 2:
            print("Número Primo")
            soma += 1
        else:
            print("Não é primo")
    return soma


primos = pergunta(10)

print(f"Foram {primos} números primos")
