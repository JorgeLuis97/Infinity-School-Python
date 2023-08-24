Agenda = {
    "LETICIA": "85 99999-9998",
    "MATHEUS": "88 98989-3333"
}


def adicionarcontato(nome, telefone):
    Agenda[nome] = telefone
    print("Contato Adicionado com sucesso!")


def editarcontato(nome):
    if nome in Agenda:
        telefone = input("Ex. 85 99999-9999 \n"
                         "Número de Contato: ")
        Agenda[nome] = telefone
        print("Contato alterado com sucesso!\n")
        print("     Lista de Contatos     ")
        for i in Agenda:
            print("----------------")
            print(f"Nome:{i} \n"
                  f"Telefone: {Agenda[i]}")
            print("----------------")
        print("                           ")
    else:
        print("Contato não Encontrado!")


def editarcontato_telefone_nome(nome):
    if nome in Agenda:
        nome1 = input("Novo nome: ").upper()
        del Agenda[nome]
        Agenda[nome1] = input("Ex. 85 99999-9999 \n"
                              "Número de Contato: ")
        print("Contato alterado com sucesso!\n")
        print("     Lista de Contatos     ")
        for i in Agenda:
            print("----------------")
            print(f"Nome:{i} \n"
                  f"Telefone: {Agenda[i]}")
            print("----------------")
        print("                           ")
    else:
        print("Contato não Encontrado!")


def editarcontato_nome(nome):
    if nome in Agenda:
        telefone1 = Agenda[nome]
        del Agenda[Nome]
        Nome2 = input("Novo Nome: ").upper()
        Agenda[Nome2] = telefone1
        print("Contato alterado com sucesso!\n")
        print("     Lista de Contatos     ")
        for i in Agenda:
            print("----------------")
            print(f"Nome:{i} \n"
                  f"Telefone: {Agenda[i]}")
            print("----------------\n")
        print("                           ")
    else:
        print("Contato não encontrado!")


def buscarcontato(nome):
    if nome in Agenda:
        print(f"Nome: {nome} \n"
              f"Telefone: {Agenda[nome]} \n")


def deletarcontato(nome):
    if nome in Agenda:
        del Agenda[nome]
        print("     Lista de Contatos     ")
        for i in Agenda:
            print("----------------")
            print(f"Nome:{i} \n"
                  f"Telefone: {Agenda[i]}")
            print("----------------\n")
        print("                           ")


def listarcontato():
    print("     Lista de Contatos     ")
    for i in Agenda:
        print("----------------")
        print(f"Nome:{i} \n"
              f"Telefone: {Agenda[i]}")
        print("----------------\n")
    print("                           ")


while True:
    print("-----Agenda Telefonica----\n")
    opcao = int(input("1 - Adicionar Contato \n"
                      "2 - Editar Contato \n"
                      "3 - Buscar Contato \n"
                      "4 - Deletar Contato \n"
                      "5 - Listar Todos \n"
                      "6 - Sair \n"
                      "--------------------------\n"
                      "Selecione uma opção: "))
    print("")
    if opcao == 1:
        Nome = input("Nome do contato: ").upper()
        Telefone = input("Ex. 85 99999-9999 \n"
                         "Número de Contato: ")
        adicionarcontato(Nome, Telefone)
        print("     Lista de Contatos     ")
        for i in Agenda:
            print("----------------")
            print(f"Nome:{i} \n"
                  f"Telefone: {Agenda[i]}")
            print("----------------")
        print("                           ")

    elif opcao == 2:
        print("     Lista de Contatos     ")
        for i in Agenda:
            print("----------------")
            print(f"Nome:{i} \n"
                  f"Telefone: {Agenda[i]}")
            print("----------------\n")
        print("                           ")
        print("-------Opções de Edição-------")
        opcaoedit = int(input("1 - Editar o Número \n"
                              "2 - Editar o Nome \n"
                              "3 - Editar Nome e Número\n"
                              "----------------------------------\n"
                              "Opção: "))
        if opcaoedit == 1:
            Nome = input("Nome do contato: ").upper()
            editarcontato(Nome)

        elif opcaoedit == 3:
            Nome = input("Nome do contato: ").upper()
            editarcontato_telefone_nome(Nome)

        elif opcaoedit == 2:
            Nome = input("Nome do contato: ").upper()
            editarcontato_nome(Nome)

    elif opcao == 3:
        print("-------Alteração de contato-------")
        print("")
        Nome = input("Nome do contato: ").upper()
        print("")
        print("                              ")
        buscarcontato(Nome)

    elif opcao == 4:
        Nome = input("Nome do contato: ").upper()
        deletarcontato(Nome)

    elif opcao == 5:
        listarcontato()

    elif opcao == 6:
        print("Saindo...")
        break
    else:
        print("!!!!!!!!!!!!!!!")
        print("Opção Invalida!")
        print("!!!!!!!!!!!!!!! \n")
