import random
from CRUD import create, read, update, delete

banco = [
    {'Matricula': 1, 'Nome': 'Leticica', 'Curso': 'Java'},
    {'Matricula': 2, 'Nome': 'Humberto', 'Curso': 'Python'}
]


adicionaraluno("Jorge", "Full")


listaralunos()

Matricula = int(input("Matricula: "))
Novo_nome = input("Novo nome: ")
Novo_curso = input("Novo curso: ")
editarAluno(Matricula, Novo_nome, Novo_curso)

print(banco)


Matricula = int(input("Matricula: "))
deletarAluno(Matricula)




print(banco)