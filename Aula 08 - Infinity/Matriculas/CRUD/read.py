def listaralunos():
    for i in banco:
        print(f"Matricula: {i['Matricula']}\n"
              f"Nome: {i['Nome']}\n"
              f"Curso: {i['Curso']}\n")


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
