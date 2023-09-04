from tkinter import *


app = Tk()
app.title("Lista")
app.geometry("300x200")
app.configure(bg="#CCCCCC")
display = Entry(app, font="Arial 10 bold")

Button()
display.pack()
frame = Frame(app)

frame_lista = Frame(app, pady=5)
frame_lista.pack(side=BOTTOM)

lista = Listbox(frame_lista, width=40)
lista.pack(side=TOP, padx=5)


app.mainloop()
