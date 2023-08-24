a = int(input("Digite o numero A: "))
b = int(input("Digite o numero B: "))
c = int(input("Digite o numero C: "))
d = int(input("Digite o numero D: "))

if b > c and d > a and c + d > a + b and c > 0 and d > 0 and a % 2 == 0:
    print(f"A = {a}, B = {b}, C = {c} e D = {d}")
    print("valores aceitos")
else:
    print(f"A = {a}, B = {b}, C = {c} e D = {d}")
    print("Valores não aceitos")
