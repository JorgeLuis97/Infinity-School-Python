# a) Implemente a função com o nome "maior_numero" e utilizando condicionais.

def maior_numero():
    n1 = int(input("Digite o 1º número: "))


n2 = int(input("Digite o 2º número: "))

if n1 > n2:
    print(f"{n1} é maior que {n2}")
else:
    print(f"{n2} é maior que {n1}")

maior_numero()

# b) Implemente a mesma função, porém utilizando a função "max".

def maior_numero():
    lista = []


n1 = int(input("Digite o 1º número: "))
lista.append(n1)
n2 = int(input("Digite o 2º número: "))
lista.append(n2)

maior = max(lista)
print(f"O Maior número é {maior}")

maior_numero()