import random


def adicionaraluno(nome: str, curso: str, banco: list) -> None:
    mat = random.randint(3, 1000)
    if mat not in banco:
        aluno = {
            'Matricula': mat,
            'Nome': nome,
            'Curso': curso
        }
        banco.append(aluno)
        print("Cadastro Realizado!!\n")
    else:
        print("Matricula já se encontra no banco!\n"
              "Favor tentar cadastro novamente\n")
