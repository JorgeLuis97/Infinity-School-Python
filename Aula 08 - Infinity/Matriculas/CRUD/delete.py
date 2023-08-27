def deletarAluno(matricula: int, banco: list) -> None:
    existe = False
    for aluno in banco:
        if aluno['Matricula'] == matricula:
            banco.remove(aluno)
            existe = True
            print('Aluno Removido!')
    if not existe:
        print("Matricula não existe!!\n")
