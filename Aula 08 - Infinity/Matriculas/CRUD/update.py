def editarAluno(matricula: int, banco: list) -> None:
    existe = False
    for aluno in banco:
        if aluno['Matricula'] == matricula:
            novo_nome = input("Novo nome: ")
            novo_curso = input("Novo curso: ")
            aluno['Nome'] = novo_nome
            aluno['Curso'] = novo_curso
            existe = True
            print('Dados Alterados!')
    if not existe:
        print("Matricula não existe!!\n")


def editarAluno_Nome(matricula: int, banco: list) -> None:
    existe = False
    for aluno in banco:
        if aluno['Matricula'] == matricula:
            novo_nome = input("Novo nome: ")
            aluno['Nome'] = novo_nome
            existe = True
            print('Dados Alterados!')
    if not existe:
        print("Matricula não existe!!\n")


def editarAluno_Curso(matricula: int, banco: list) -> None:
    existe = False
    for aluno in banco:
        if aluno['Matricula'] == matricula:
            novo_curso = input("Novo curso: ")
            aluno['Curso'] = novo_curso
            existe = True
            print('Dados Alterados!')
    if not existe:
        print("Matricula não existe!!\n")
