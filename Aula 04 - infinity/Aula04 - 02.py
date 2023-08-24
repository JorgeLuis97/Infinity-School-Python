# 2. Escreva uma função que recebe dois parametros,
# base e altura, em seguida calcule a área do triangulo e exiba o resultado na tela

base = int(input("Digite a Base: "))
altura = int(input("Digite a Altura: "))


def area_triangulo(n1, n2):
    return n1 * n2 / 2


area = area_triangulo(base, altura)

print(f"A area do triangulo é {area}")
