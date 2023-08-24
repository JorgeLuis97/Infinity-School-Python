# 3. Escreva uma função que recebe três parametros, base maior, base menor
# e altura, em seguida calcule a área do trapézio e exiba o resultado na tela
# area = (base maior + base menor) * altura / 2

baseMaior = int(input("Digite a Base Maior: "))
baseMenor = int(input("Digite a Base Menor: "))
altura = float(input("Digite a altura: "))


def area_trapezio(n1, n2, n3):
    return (n1 + n2) * n3 / 2


area = area_trapezio(baseMaior, baseMenor, altura)

print(f"A area do trapezio é {area}")
