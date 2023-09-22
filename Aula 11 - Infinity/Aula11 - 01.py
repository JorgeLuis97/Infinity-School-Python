from tkinter import *
from tkinter import messagebox
from tkinter import ttk

app = Tk()

app.title("Agenda Telefonica")

# Storage
agenda = []
index = 0


# Funções

def adicionar() -> None:
    numero = txt_numero.get()
    nome = txt_nome.get()
    categoria = cb_categorias.get()
    if numero == "":
        messagebox.showinfo("Erro!",
                            "Número Vazio")
    elif nome == "":
        messagebox.showinfo("Erro!",
                            "Nome Vazio")
    elif categoria == "":
        messagebox.showinfo("Erro!",
                            "Escolha uma categoria")
    else:
        limparcampos()
        contato = {
            "Nome": nome,
            "Telefone": numero,
            "Categoria": categoria
        }
        agenda.append(contato)
        atualizartabela()
        messagebox.showinfo("SUCESSO!!",
                            "Adicionado com Sucesso!")


def atualizartabela() -> None:
    for linha in lista.get_children():
        lista.delete(linha)

    for contato in agenda:
        lista.insert("", END, values=(contato["Nome"],
                                      contato["Telefone"],
                                      contato["Categoria"]))


def editarcontato() -> None:
    agenda[index] = {
        "Nome": txt_nome.get(),
        "Telefone": txt_numero.get(),
        "Categoria": cb_categorias.get()
    }
    limparcampos()
    atualizartabela()
    messagebox.showinfo("Sucesso!!",
                        "Dados Alterados com sucesso!")

def listaclique(event) -> None:
    selecionar = lista.selection()
    global index
    index = lista.index(selecionar[0])
    contato = agenda[index]
    limparcampos()
    txt_nome.insert(0, contato['Nome'])
    txt_numero.insert(0, contato['Telefone'])
    cb_categorias.insert(0, contato['Categoria'])

def deletarcontato() -> None:
    selecionar = lista.selection()
    if selecionar:
        agenda.remove(agenda[index])
        messagebox.showinfo("Sucesso!",
                            "Deletado com Sucesso")
        limparcampos()
        atualizartabela()
    else:
        messagebox.showinfo("Erro",
                            "Nada Selecionado")


def limparcampos() -> None:
    txt_nome.delete(0, END)
    txt_numero.delete(0, END)
    cb_categorias.set("")

# Frame


frame_lista = Frame(app)
frame_lista.grid(row=2, column=0, pady=5)
frame_registro = Frame(app)
frame_registro.grid(row=0, column=0, pady=5)

# Labels
label_nome = Label(frame_registro, text="Nome:", fg="red", font="Tahoma 10 bold")
label_nome.grid(row=0, column=0)
label_numero = Label(frame_registro, text="Numero:", fg="red", font="Tahoma 10 bold")
label_numero.grid(row=0, column=2)

label_lista = Label(frame_lista, text="Lista Telefonica", fg="red", font="Tahoma 10 bold")
label_lista.grid(row=0, pady=8)

label_categorias = Label(frame_registro, text="Categorias:", fg="red", font="Tahoma 10 bold")
label_categorias.grid(row=1, column=0, pady=5)

# entry
txt_nome = Entry(frame_registro, fg="red", font="Tahoma 10 bold")
txt_nome.grid(row=0, column=1, padx=5)
txt_numero = Entry(frame_registro, fg="red", font="Tahoma 10 bold")
txt_numero.grid(row=0, column=3, padx=5)

# Treeview\Tabela
colunas = ["Nome", "Telefone", "Categoria"]
lista = ttk.Treeview(frame_lista, columns=colunas, show="headings")
for colunas in colunas:
    lista.heading(colunas, text=colunas)

lista.grid(row=1, columnspan=1, padx=8)

lista.bind("<ButtonRelease-1>", listaclique)

# Botões
adicionar_botao = Button(frame_registro, text="Adicionar", command=lambda: adicionar())
adicionar_botao.grid(row=1, column=2, padx=5, pady=5)

deletar_botao = Button(frame_lista, text="Deletar", command=lambda: deletarcontato())
deletar_botao.grid(row=1, column=2, padx=5)

editar_botao = Button(frame_lista, text="Editar", command=lambda: editarcontato())
editar_botao.grid(row=1, column=1, padx=5)

limpar_botao = Button(frame_registro, text="Limpar", command=lambda: limparcampos())
limpar_botao.grid(row=1, column=3, padx=5, pady=5)


# combobox
categorias = ["Amigos", "Familia", "Trabalho"]
cb_categorias = ttk.Combobox(frame_registro, values=categorias)
cb_categorias.grid(row=1, column=1, padx=5, pady=5)

app.mainloop()
