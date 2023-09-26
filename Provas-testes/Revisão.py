# [PY-A07]Você foi contratado para desenvolver um programa que calcule a média de notas dos alunos de uma turma.
# Para isso, você deverá criar uma lista com as notas de cada aluno e,
# em seguida, implementar uma função que calcule a média aritmética das notas.
# Além disso, você deverá utilizar um loop while para pedir ao usuário que insira as notas dos alunos
# até que ele decida parar. Por fim, você deverá utilizar um loop for para imprimir a média de cada aluno.
#
# a) Escreva o código para a função que calcule a média aritmética das notas.
#
# b) Escreva o código para o loop while que pede ao usuário que insira as notas dos alunos.
#
# c) Escreva o código para o loop for que imprime a média de cada aluno.

aluno1 = []
aluno2 = []
aluno3 = []

while True:
    menu = int(input("1 - Inserir nota de aluno\n"
                 "2 - Media das Notas\n"
                 "3 - Sair\n"
                 "Opção: "))
    if menu == 1:
        opcoes = int(input("1 - 1º Aluno\n"
                       "2 - 2º Aluno\n"
                       "3 - 3º Aluno\n"
                       "Opção: "))
        if opcoes == 1:
            nota = float(input("Nova Nota: "))
            aluno1.append(nota)
            print("Nota Adicionada ao 1º Aluno\n")
        elif opcoes == 2:
            nota = float(input("Nova Nota: "))
            aluno2.append(nota)
            print("Nota Adicionada ao 2º Aluno\n")
        elif opcoes == 3:
            nota = float(input("Nova Nota: "))
            aluno3.append(nota)
            print("Nota Adicionada ao 3º Aluno\n")
    elif menu == 2:
        print("------ Media de Notas ------\n")
        print(f"Media do 1º ALuno: {sum(aluno1) / len(aluno1)}\n")
        print(f"Media do 2º ALuno: {sum(aluno2) / len(aluno2)}\n")
        print(f"Media do 3º ALuno: {sum(aluno3) / len(aluno3)}\n")
        print("--------------------------\n")
    elif menu == 3:
        print("Saindo...")
        break