import random
from CRUD import create, read

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


adicionaraluno("Jorge", "Full")


def listaralunos():
    for i in banco:
        print(f"Matricula: {i['Matricula']}\n"
              f"Nome: {i['Nome']}\n"
              f"Curso: {i['Curso']}\n")


listaralunos()


def buscarAlunoMat(matricula: int) -> None:
    existe = False
    for aluno in banco:
        if aluno['Matricula'] == matricula:
            print(f"Matricula: {aluno['Matricula']}\n"
                  f"Nome: {aluno['Nome']}\n"
                  f"Curso: {aluno['Curso']}\n")
            existe = True
    if existe == False:
        print("Matricula não existe!!")


Matricula = int(input("Matricula: "))
buscarAlunoMat(Matricula)


def editarAluno(matricula: int, novo_nome: str, novo_curso: str) -> None:
    existe = False
    for aluno in banco:
        if aluno['Matricula'] == matricula:
            aluno['Nome'] = novo_nome
            aluno['Curso'] = novo_curso
            existe = True
            print('Dados Alterados!')
    if existe == False:
        print("Matricula não existe!!")


Matricula = int(input("Matricula: "))
Novo_nome = input("Novo nome: ")
Novo_curso = input("Novo curso: ")
editarAluno(Matricula, Novo_nome, Novo_curso)

print(banco)
def deletarAluno(matricula: int) ->None:
    existe = False
    for aluno in banco:
        if aluno['Matricula'] == matricula:
            banco.remove(aluno)
            existe = True
            print('Aluno Removido!')
    if existe == False:
        print("Matricula não existe!!")

Matricula = int(input("Matricula: "))
deletarAluno(Matricula)




print(banco)