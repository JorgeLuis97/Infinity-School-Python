from tkinter import messagebox
from tkinter import ttk
from customtkinter import *

app = CTk()

app.title("Agenda Telefonica")


set_appearance_mode(
    "System"
)

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
    messagebox.showinfo("Guia", "Caso queira editar contato favor alterar no campo registro e"
                                " depois apertar em Editar")
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
frame_lista = CTkFrame(master=app)
frame_lista.grid(row=2, column=0, pady=5)
frame_registro = CTkFrame(master=app)
frame_registro.grid(row=0, column=0, pady=5)

# Labels
label_nome = CTkLabel(master=frame_registro, text="Nome:", font=("Tahoma", 10))
label_nome.grid(row=0, column=0)
label_numero = CTkLabel(master=frame_registro, text="Numero:", font=("Tahoma", 10))
label_numero.grid(row=0, column=2)

label_lista = CTkLabel(master=frame_lista, text="Lista Telefonica", font=("Tahoma", 10))
label_lista.grid(row=0, pady=8)

label_categorias = CTkLabel(master=frame_registro, text="Categorias:", font=("Tahoma", 10))
label_categorias.grid(row=1, column=0, pady=5, padx=5)

# entry
txt_nome = CTkEntry(master=frame_registro, font=("Tahoma", 10), width=100)
txt_nome.grid(row=0, column=1, padx=5)
txt_numero = CTkEntry(master=frame_registro, font=("Tahoma", 10), width=100)
txt_numero.grid(row=0, column=3, padx=5)

# Treeview\Tabela
colunas = ["Nome", "Telefone", "Categoria"]
lista = ttk.Treeview(frame_lista, columns=colunas, show="headings")
for colunas in colunas:
    lista.heading(colunas, text=colunas)

lista.grid(row=1, columnspan=1, padx=8)

lista.bind("<ButtonRelease-1>", listaclique)

# BotõesCTk
adicionar_botao = CTkButton(master=frame_registro, text="Adicionar", command=lambda: adicionar(), width=80,
                            fg_color=("gray", "blue"), hover=True, hover_color=("#DB3E39", "#821D1A"))

adicionar_botao.grid(row=1, column=2, padx=5, pady=5)

deletar_botao = CTkButton(master=frame_lista, text="Deletar", command=lambda: deletarcontato(), width=80,
                          fg_color=("gray", "blue"), hover=True, hover_color=("#DB3E39", "#821D1A"))

deletar_botao.grid(row=1, column=2, padx=5)

editar_botao = CTkButton(master=frame_lista, text="Editar", command=lambda: editarcontato(), width=80,
                         fg_color=("gray", "blue"), hover=True, hover_color=("#DB3E39", "#821D1A"))

editar_botao.grid(row=1, column=1, padx=5)

limpar_botao = CTkButton(master=frame_registro, text="Limpar", command=lambda: limparcampos(), width=80,
                         fg_color=("gray", "blue"), hover=True, hover_color=("#DB3E39", "#821D1A"))

limpar_botao.grid(row=1, column=3, padx=5, pady=5)

# combobox
categorias = ["Amigos", "Familia", "Trabalho"]
cb_categorias = ttk.Combobox(frame_registro, values=categorias, width=15)
cb_categorias.grid(row=1, column=1, padx=5, pady=5)



app.mainloop()