# 2. Escreva uma função que recebe três parametros, dois valores e uma operação (string).
# Em seguida realize a operação entre os dois valores e retorne o resultado. Em seguida imprima o resultado na tela
# calculadora(10, 5, "+") => 15
def operacao(valor1, valor2, operacao: str):
    if operacao == "/":
        return valor1 / valor2
    elif operacao == "*":
        return valor1 * valor2
    elif operacao == "+":
        return valor1 + valor2
    elif operacao == "-":
        return valor1 - valor2


print("Soma = +\n"
      "Multiplicação = *\n"
      "Divisão = /\n"
      "Subtração = -\n")
ope = input("Qual operação: ")
print("")
n1 = int(input("1º número: "))
n2 = int(input("2º número: "))

resultado = operacao(n1, n2, ope)

print(f"{n1} {ope} {n2} = {resultado}")
