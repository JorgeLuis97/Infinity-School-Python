import math
a = int(input("Digite o numero A: "))
b = int(input("Digite o numero B: "))
c = int(input("Digite o numero C: "))

delta = b ** 2 - 4 * a * c

print(f"Delta = {delta}\n")


if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"Primeira Raiz: {x1}\n"
          f"Segunda Raiz: {x2}")
elif delta < 0:
    print("Não existe Raiz Real")
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    print(f"Raiz: {x1}")
