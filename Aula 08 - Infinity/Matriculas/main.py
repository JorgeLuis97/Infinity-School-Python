import random

banco = [
    {'Matricula': 1, 'Nome': 'Leticica', 'Curso': 'Java'},
    {'Matricula': 2, 'Nome': 'Humberto', 'Curso': 'Python'}
]


def adicionaraluno(nome: str, curso: str) -> None:
    mat = random.randint(3, 1000)
    aluno = {
        'Matricula': mat,
        'Nome': nome,
        'Curso': curso
    }
    banco.append(aluno)
    print("Cadastro Realizado!!")
