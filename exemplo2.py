import tkinter as tk

def digitar_7():
    visor.insert(tk.END, "7")

def digitar_8():
    visor.insert(tk.END, "8")

def digitar_9():
    visor.insert(tk.END, "9")


janela = tk.Tk()
janela.title("Teclado da calculadora")

botao_7 = tk.Button(janela, text="7", width=6, command=digitar_7)
botao_7.grid(row=1,column=0, padx=2, pady=2)

botao_8 = tk.Button(janela, text="8", width=6, command=digitar_8)
botao_8.grid(row=1,column=1, padx=2, pady=2)

botao_9 = tk.Button(janela, text="9", width=6, command=digitar_9)
botao_9.grid(row=1,column=2, padx=2, pady=2)

visor = tk.Entry(janela, width=24, justify="right")
visor.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

janela.mainloop()