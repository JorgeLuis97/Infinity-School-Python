import random
x = random.randint(-100, 100)
y = random.randint(-100, 100)

if x > 0 and y > 0:
    print(f"X = {x} e Y = {y}")
    print("Está no primeiro quadrante")
elif x < 0 < y:
    print(f"X = {x} e Y = {y}")
    print("Está no segundo quadrante")
elif x < 0 and y < 0:
    print(f"X = {x} e Y = {y}")
    print("Está no terceiro quadrante")
elif y < 0 < x:
    print(f"X = {x} e Y = {y}")
    print("Está no Quarto quadrante")
else:
    print(f"X = {x} e Y = {y}")
    print("Está no meio")
