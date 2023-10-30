# Crie uma janela usando a biblioteca TKINTER em Python
# que tenha um título "Sistema de Cadastro". Nesta janela,
# crie um campo de entrada de texto para o usuário digitar seu nome e um botão "Enviar"
# que, ao ser clicado, exiba uma mensagem de boas-vindas com o nome do usuário em uma nova janela.


from tkinter import *
from tkinter import messagebox

app = Tk()

def message():
    messagebox.showinfo("Sucesso", f"Bem vindo {nome_entry.get()}")

app.title("Sistema de Cadastro")

nome_label = Label(app, text="Nome:")
nome_label.grid(row=0, column=0)

nome_entry = Entry(app)
nome_entry.grid(row=0, column=1)

enviar_button = Button(app, text="Enviar", command= message)
enviar_button.grid(row=1, column=1)

app.mainloop()
