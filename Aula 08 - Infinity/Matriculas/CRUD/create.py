import random

def adicionaraluno(nome: str, curso: str) -> None:
    mat = random.randint(3, 1000)
    aluno = {
        'Matricula': mat,
        'Nome': nome,
        'Curso': curso
    }
    banco.append(aluno)
    print("Cadastro Realizado!!")


