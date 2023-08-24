n = int(input("Digite um numero: "))
soma = 0
for i in range(1, n+1):
    if n % i == 0:
        soma += 1
        print(soma)

if soma == 2:
    print("Número primo")
else:
    print("Não primo")
