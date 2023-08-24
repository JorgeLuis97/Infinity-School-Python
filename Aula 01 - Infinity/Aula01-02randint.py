import random
a = random.randint(1, 10)
b = random.randint(1, 10)
c = random.randint(1, 10)

if a == b and a == c:
    print(f"A = {a}, B = {b} e C = {c}")
    print("É equilatero")
elif a == b and a != c or b == c and b != a or c == a and c != b:
    print(f"A = {a}, B = {b} e C = {c}")
    print("É Isoceles")
elif a != b and a != c:
    print(f"A = {a}, B = {b} e C = {c}")
    print("É Escaleno")
