from tkinter import *


def limpar() -> None:
    display.delete(0, END)


def inserir(valor: str) -> None:
    display.insert(END, valor)


def calcular() -> None:
    texto_display = display.get()
    resultado = eval(texto_display)
    display.delete(0, END)
    display.insert(0, str(resultado))


window = Tk()
window.title("Calculadora")

display = Entry(window, font="Arial 20 bold",
                bg="#1c3ec7",fg="white", width=19)
display.pack()
frame = Frame(window)
# botões
btn_0 = Button(frame, text="0", bg="orange",
               font="Arial 16 bold", fg="white",
               height=3, width=5,
               command=lambda: inserir('0'))
btn_1 = Button(frame, text="1", bg="orange",
               font="Arial 16 bold", fg="white",
               height=3, width=5,
               command=lambda: inserir('1'))
btn_2 = Button(frame, text="2", bg="orange",
               font="Arial 16 bold", fg="white",
               height=3, width=5,
               command=lambda: inserir('2'))
btn_3 = Button(frame, text="3", bg="orange",
               font="Arial 16 bold", fg="white",
               height=3, width=5,
               command=lambda: inserir('3'))
btn_4 = Button(frame, text="4", bg="orange",
               font="Arial 16 bold", fg="white",
               height=3, width=5,
               command=lambda: inserir('4'))
btn_5 = Button(frame, text="5", bg="orange",
               font="Arial 16 bold", fg="white",
               height=3, width=5,
               command=lambda: inserir('5'))
btn_6 = Button(frame, text="6", bg="orange",
               font="Arial 16 bold", fg="white",
               height=3, width=5,
               command=lambda: inserir('6'))
btn_7 = Button(frame, text="7", bg="orange",
               font="Arial 16 bold", fg="white",
               height=3, width=5,
               command=lambda: inserir('7'))
btn_8 = Button(frame, text="8", bg="orange",
               font="Arial 16 bold", fg="white",
               height=3, width=5,
               command=lambda: inserir('8'))
btn_9 = Button(frame, text="9", bg="orange",
               font="Arial 16 bold", fg="white",
               height=3, width=5,
               command=lambda: inserir('9'))
btn_somar = Button(frame, text="+", bg="orange",
                   font="Arial 16 bold", fg="white",
                   height=3, width=5,
                   command=lambda: inserir('+'))
btn_sub = Button(frame, text="-", bg="orange",
                 font="Arial 16 bold", fg="white",
                 height=3, width=5,
                 command=lambda: inserir('-'))
btn_mult = Button(frame, text="*", bg="orange",
                  font="Arial 16 bold", fg="white",
                  height=3, width=5,
                  command=lambda: inserir('*'))
btn_div = Button(frame, text="/", bg="orange",
                 font="Arial 16 bold", fg="white",
                 height=3, width=5,
                 command=lambda: inserir('/'))
btn_limpar = Button(frame, text="C", bg="orange",
                    font="Arial 16 bold", fg="white",
                    height=3, width=5, command=limpar)
btn_igual = Button(frame, text="=", bg="orange",
                   font="Arial 16 bold", fg="white",
                   height=3, width=5, command=calcular)
frame.pack()
# Primeira fileira
btn_7.grid(row=0, column=0)
btn_8.grid(row=0, column=1)
btn_9.grid(row=0, column=2)
btn_mult.grid(row=0, column=3)

# Segunda fileira
btn_4.grid(row=1, column=0)
btn_5.grid(row=1, column=1)
btn_6.grid(row=1, column=2)
btn_sub.grid(row=1, column=3)

# Terceira fileira
btn_1.grid(row=2, column=0)
btn_2.grid(row=2, column=1)
btn_3.grid(row=2, column=2)
btn_somar.grid(row=2, column=3)

# Quarta fileira
btn_limpar.grid(row=3, column=0)
btn_igual.grid(row=3, column=1)
btn_0.grid(row=3, column=2)
btn_div.grid(row=3, column=3)

window.mainloop()
