a = float(input("digite o numero 1: "))
b = float(input("digite o numero 2: "))
print("-------------------------------")
print("SOMA = 1 ou soma\n"
      "Subtração = 2 ou sub\n"
      "Multiplicação = 3 ou multi\n"
      "Divisão = 4 ou div\n")
print("-------------------------------")

operacao = input("Digite qual operação: ").upper()

if operacao == "1" or operacao == "SOMA":
    resultado = a + b
    print(f"A soma de {a} + {b} é {resultado}")
elif operacao == "2" or operacao == "SUB":
    resultado = a - b
    print(f"A Subtração de {a} - {b} é {resultado}")
elif operacao == "3" or operacao == "MULTI":
    resultado = a * b
    print(f"A Multiplicação de {a} * {b} é {resultado}")
elif operacao == "4" or operacao == "DIV":
    resultado = a / b
    print(f"A Divisão de {a} / {b} é {resultado}")
