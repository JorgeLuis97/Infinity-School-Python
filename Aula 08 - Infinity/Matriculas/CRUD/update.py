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