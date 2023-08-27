def deletarAluno(matricula: int) ->None:
    existe = False
    for aluno in banco:
        if aluno['Matricula'] == matricula:
            banco.remove(aluno)
            existe = True
            print('Aluno Removido!')
    if existe == False:
        print("Matricula não existe!!")