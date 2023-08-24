salario = []
idade = []
Sexo = []

while True:
    print("(M) Masculino e (F) Feminino")
    idade1 = int(input("Idade: "))
    if idade1 < 0:
        break
    idade.append(idade1)
    sexo1 = input("Sexo: ").upper()
    Sexo.append(sexo1)
    salario1 = float(input("Salario: "))
    salario.append(salario1)

maior_salario = max(salario)
maior_idade = max(idade)
menor_salario = min(salario)
menor_idade = min(idade)
mulheres = Sexo.count("F")
soma_salario = sum(salario)
media_salario = soma_salario / len(salario)
index = salario.index(menor_salario)

print(f"Esse é o Maior Salario:{maior_salario}\n")
print(f"Esse é a Maior idade: {maior_idade}\n")
print(f"Esse é o menor Salario:{menor_salario}\n")
print(f"Essa é a menor idade: {menor_idade}\n")
print(f"Tem {mulheres} Mulheres\n")
print(f"Essa é a média salarial: {media_salario:.2f}\n")
print(f"O sexo da pessoa com menor salario: {Sexo[index]}\n")
print(f"A Idade da pessoa com menor salario:{idade[index]}\n")
