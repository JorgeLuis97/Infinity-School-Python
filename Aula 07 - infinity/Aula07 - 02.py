# 2. Crie uma nova chave no dicionario do exercio anterior chamada "salario" e digite o salario nela.

dicionario = {
    'Nome': 'Jorge Luis Gomes Rabelo',
    'Idade': 25,
    'Profissao': 'Analista de Suporte',
}

dicionario['Salario'] = float(input("Salario: "))

for i in dicionario:
    print(f"{i}: {dicionario[i]}")
