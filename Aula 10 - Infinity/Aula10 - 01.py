from tkinter import *
from tkinter import messagebox

app = Tk()

app.title("Lista")
app.geometry("310x250")

#Função

def delete():
    lista.delete()


def inserir():
    nome = entry.get()
    lista.insert(END, nome)
    entry.delete(0, END)
    messagebox.showinfo("Adcionado",
                        "Adicionado a Lista com sucesso!")


#Labels
label = Label(app, text="Nome:", foreground="red", font="Tahoma 10 bold")
label.grid(row=0, column=0, pady=8, padx=5)

#Entry
entry = Entry(app, width=25)
entry.grid(row=0, column=1, padx=8, pady=8)

#Lista
lista = Listbox(app, font="Tahoma 10 bold")
lista.grid(row=1, column=1, pady=15)

#Button
button_Adicionar = Button(app, text="Adicionar", command=lambda: inserir())
button_Adicionar.grid(row=0, column=3, padx=8, pady=8)


app.mainloop()
