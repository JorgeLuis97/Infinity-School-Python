from CRUD import create, read, update, delete

banco = [
    {'Matricula': 1, 'Nome': 'Leticica', 'Curso': 'Java'},
    {'Matricula': 2, 'Nome': 'Humberto', 'Curso': 'Python'}
]


while True:
    opcao = int(input("---------Opções--------\n"
                      "1 - Adicionar Aluno\n"
                      "2 - Editar Aluno\n"
                      "3 - Buscar Aluno\n"
                      "4 - Listar Alunos\n"
                      "5 - Deletar Aluno\n"
                      "6 - Sair\n"
                      "----------------------\n"
                      "\nSelecione a Opção: "))
    if opcao == 1:
        print("")
        nome = input("Nome do Aluno: ")
        curso = input("Curso do Aluno: ")
        create.adicionaraluno(nome, curso, banco)
    elif opcao == 2:
        print("\n-------Opções de Edição-------\n")
        opcaoedit = int(input("1 - Editar o Nome\n"
                              "2 - Editar Curso\n"
                              "3 - Editar Nome e Curso\n"
                              "\n----------------------------------\n"
                              "\nSelecione a Opção: "))
        if opcaoedit == 1:
            Matricula = int(input("Buscar Matricula: "))
            update.editarAluno_Nome(Matricula, banco)

        elif opcaoedit == 2:
            Matricula = int(input("Buscar Matricula: "))
            update.editarAluno_Curso(Matricula, banco)

        elif opcaoedit == 3:
            Matricula = int(input("Buscar Matricula: "))
            update.editarAluno(Matricula, banco)

    elif opcao == 3:
        print("")
        Matricula = int(input("Buscar Matricula: "))
        read.buscarAlunoMat(Matricula, banco)
    elif opcao == 4:
        print("")
        read.listaralunos(banco)
    elif opcao == 5:
        print("")
        Matricula = int(input("Buscar Matricula: "))
        delete.deletarAluno(Matricula, banco)
    elif opcao == 6:
        print("\nSaindo...\n")
        break
    else:
        print("\nOpção Invalida!!\n")
