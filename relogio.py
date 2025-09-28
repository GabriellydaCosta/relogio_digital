from tkinter import *
from tkinter import ttk
from datetime import datetime 

import pyglet
pyglet.font.add_file("digital-7.ttf")

#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

fundo = "#A23AC3"
fonte = "#FFFFFF"

janela = Tk()
janela.title("Relógio Digital")
janela.geometry("440x180")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=fundo)
janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(1, weight=1)
janela.grid_columnconfigure(0, weight=1)


def relogio():
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b")
    ano = tempo.strftime("%Y")

    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=dia_semana + " " + str(dia) + "/" + str(mes) + "/" + str(ano))

l1=Label(janela, text="", font=("digital-7", 80), bg =fundo, fg=fonte)
l1.grid(row=0, column=0, sticky=NSEW, padx=5)

l2=Label(janela, text="", font=("digital-7", 20), bg =fundo, fg=fonte)
l2.grid(row=1, column=0, sticky=NSEW, padx=5)

relogio()
janela.mainloop()


