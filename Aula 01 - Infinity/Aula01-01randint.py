import random
a = random.randint(-100, 100)
b = random.randint(-100, 100)
c = random.randint(-100, 100)
d = random.randint(-100, 100)

if b > c and d > a and c + d > a + b and c > 0 and d > 0 and a % 2 == 0:
    print(f"A = {a}, B = {b}, C = {c} e D = {d}")
    print("valores aceitos")
else:
    print(f"A = {a}, B = {b}, C = {c} e D = {d}")
    print("Valores não aceitos")
