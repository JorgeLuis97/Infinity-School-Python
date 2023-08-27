pessoas = {
    "João": 23,
    "Maria": 28,
    "Pedro": 35,
    "Lucas": 19
}

# a) Acesse a idade da pessoa "João" e armazene em uma variável chamada idade_joao.
idade_joao = pessoas['João']
# b) Adicione uma nova pessoa ao dicionário com nome "Ana" e idade 31.
pessoas["Ana"] = 31
# c) Crie uma função chamada maior_idade que recebe um dicionário como argumento e
# retorna o nome da pessoa com a maior idade.


def maior_idade(Pessoas: dict) -> int:
    maior = 0
    for i in Pessoas:
        if Pessoas[i] > maior:
            maior = Pessoas[i]
    return maior


teste_maior = maior_idade(pessoas)

print(f"Maior idade: {teste_maior}")