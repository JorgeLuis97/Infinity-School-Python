import pymysql.cursors
from pymysql import *

try:
    conexao = connect(host="localhost", user="root", password="", db="escola", cursorclass=pymysql.cursors.DictCursor)

    print("\nConexão estabelecida..\n")


except Exception as error:
    print(error)

cursor = conexao.cursor()


def select():
    try:
        sql = "SELECT * FROM alunos"
        cursor.execute(sql)
        alunos = cursor.fetchall()
        for aluno in alunos:
            # noinspection PyTypeChecker
            print(f"Nome: {aluno['Nome']}, Idade: {aluno['Idade']};\n")
    except Exception as error2:
        print(error2)


def insert(nome, idade, nota, curso):
    try:
        sql = "INSERT INTO alunos (nome, idade, curso, nota) VALUES" \
              "(%s, %s, %s, %s)"
        cursor.execute(sql, (nome, idade, curso, nota))
        conexao.commit()
        print("\nAluno adicionado\n")
    except Exception as error3:
        print(error3)

def validador(id):
    select_validador = "SELECT * FROM alunos WHERE ID = %s"
    cursor.execute(select_validador, id)
    validador = cursor.fetchall()
    if validador:
        return True
    else:
        return False

def update(nome, idade, curso, nota, id):
    try:
        validar = validador(id)
        if validar:
            sql = "UPDATE alunos set Nome = %s, Idade = %s, Curso = %s, nota = %s WHERE id = %s"
            cursor.execute(sql, (nome, idade, curso, nota, id))
            conexao.commit()
        else:
            print("Aluno não encontrado")
    except Exception as error4:
        print(error4)


def delete(id):
    try:
        validar = validador(id)

        if validar:
            sql = "DELETE FROM alunos where ID ='%s'"
            cursor.execute(sql, id)
            conexao.commit()
            print("Aluno deletado")
        else:
            print("Aluno não encontrado")
    except Exception as error5:
        print(error5)


# insert("JAJA", 55, "Python", 8.5)
# delete(3)
update("Jorge Luis", 28, "Nenhum", 10, 1)
select()
