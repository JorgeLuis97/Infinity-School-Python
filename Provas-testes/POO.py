# crie uma classe utilizando os conceitos de POO das aulas passadas.
#
# Para criar sua classe, pense em uma entidade do mundo real que possa ser representada de maneira simples e objetiva.
#
# Por exemplo, uma classe "Pessoa"
# poderia ter atributos como nome, idade e endereço, e métodos como cumprimentar e se movimentar.
#
# Já uma classe "Animal" poderia ter atributos como espécie, peso e altura, e métodos como andar e dormir.

class Pessoa:
    def __init__(self, nome, idade, endereco, renda, altura):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.renda = renda
        self.altura = altura

class Cargo(Pessoa):
    def __init__(self, salario, cargo):
        super().__init__(nome, idade)
        self.salario = salario
        self.cargo = cargo