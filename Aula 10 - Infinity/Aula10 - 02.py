from tkinter import *


app = Tk()

# noinspection SpellCheckingInspection
app.title("Calculadora")
# app.geometry("250x380")

#Função


def limpar():
    display.delete(0, END)


def inserir(valor: str) -> None:
    display.insert(END, valor)


def calcular():
    nome_display = display.get()
    resultado = eval(nome_display)
    display.delete(0, END)
    display.insert(0, str(resultado))


#Frame
frame_button = Frame(app)
frame_button.pack(pady=30)


#Entry
display = Entry(app, width=250, bg="Black", font="Arial 20 bold", fg="White",)
display.place(y=5)

#Button
btn_0 = Button(frame_button, text="0", bg="Gray", font="Arial 12 bold", fg="White", height=3, width=5,
               command=lambda: inserir("0"))

btn_1 = Button(frame_button, text="1", bg="Gray", font="Arial 12 bold", fg="White", height=3, width=5,
               command=lambda: inserir("1"))

btn_2 = Button(frame_button, text="2", bg="Gray", font="Arial 12 bold", fg="White", height=3, width=5,
               command=lambda: inserir("2"))

btn_3 = Button(frame_button, text="3", bg="Gray", font="Arial 12 bold", fg="White", height=3, width=5,
               command=lambda: inserir("3"))

btn_4 = Button(frame_button, text="4", bg="Gray", font="Arial 12 bold", fg="White", height=3, width=5,
               command=lambda: inserir("4"))

btn_5 = Button(frame_button, text="5", bg="Gray", font="Arial 12 bold", fg="White", height=3, width=5,
               command=lambda: inserir("5"))

btn_6 = Button(frame_button, text="6", bg="Gray", font="Arial 12 bold", fg="White", height=3, width=5,
               command=lambda: inserir("6"))

btn_7 = Button(frame_button, text="7", bg="Gray", font="Arial 12 bold", fg="White", height=3, width=5,
               command=lambda: inserir("7"))

btn_8 = Button(frame_button, text="8", bg="Gray", font="Arial 12 bold", fg="White", height=3, width=5,
               command=lambda: inserir("8"))

btn_9 = Button(frame_button, text="9", bg="Gray", font="Arial 12 bold", fg="White", height=3, width=5,
               command=lambda: inserir("9"))

btn_igual = Button(frame_button, text="=", bg="Gray", font="Arial 12 bold", fg="White", height=3, width=5,
                   command=calcular)

btn_limpar = Button(frame_button, text="C", bg="Gray", font="Arial 12 bold", fg="White", height=3, width=5,
                    command=limpar)

btn_soma = Button(frame_button, text="+", bg="Gray", font="Arial 12 bold", fg="White", height=3, width=5,
                  command=lambda: inserir("+"))

btn_multi = Button(frame_button, text="*", bg="Gray", font="Arial 12 bold", fg="White", height=3, width=5,
                   command=lambda: inserir("*"))

btn_div = Button(frame_button, text="%", bg="Gray", font="Arial 12 bold", fg="White", height=3, width=5,
                 command=lambda: inserir("/"))

btn_sub = Button(frame_button, text="-", bg="Gray", font="Arial 12 bold", fg="White", height=3, width=5,
                 command=lambda: inserir("-"))

# Primeira Fileira
btn_7.grid(row=0, column=0)
btn_8.grid(row=0, column=1)
btn_9.grid(row=0, column=2)
btn_multi.grid(row=0, column=3)

# Segunda Fileira
btn_4.grid(row=1, column=0)
btn_5.grid(row=1, column=1)
btn_6.grid(row=1, column=2)
btn_sub.grid(row=1, column=3)

#terceira fileira
btn_1.grid(row=2, column=0)
btn_2.grid(row=2, column=1)
btn_3.grid(row=2, column=2)
btn_soma.grid(row=2, column=3)

#Quarta Fileira
btn_limpar.grid(row=3, column=0)
btn_igual.grid(row=3, column=1)
btn_0.grid(row=3, column=2)
btn_div.grid(row=3, column=3)

app.mainloop()
