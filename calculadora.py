import tkinter as tk

num1 = 0

operacao = ""

def digitar(num):
    num_atual = visor.get()
    if(num_atual == 0):
        visor.delete(0, tk.END)
    visor.insert(tk.END, num)

def conta(sinal):
    if(sinal != "-" or operacao == ""):
        num1 = visor.get()
        visor.delete(0, tk.END)
        print(num1)
        operacao = sinal

def resultado():
    num2 = visor.get()
    result = float(num1,operacao,num2)
    visor.insert(result)

def apagar():
    visor.delete(0, tk.END)
    visor.insert(tk.END,0)

janela = tk.Tk()
janela.title("Teclado da calculadora")

visor = tk.Entry(janela, width=36, justify="right")
visor.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

botao_C = tk.Button(janela, text="C", width=6, command=apagar)
botao_C.grid(row=1,column=0 , padx=2, pady=2)

botao_del = tk.Button(janela, text="⌫", width=6, command=lambda: digitar(1))
botao_del.grid(row=1,column=1, padx=2, pady=2)

botao_div = tk.Button(janela, text="÷", width=6, command=lambda: digitar(2))
botao_div.grid(row=1,column=2, padx=2, pady=2)

botao_mult = tk.Button(janela, text="x", width=6, command=lambda: digitar(3))
botao_mult.grid(row=1,column=3, padx=2, pady=2)

botao_0 = tk.Button(janela, text="0", width=14, command=lambda: digitar(0))
botao_0.grid(row=5,column=0, columnspan=2 , padx=2, pady=2)

botao_1 = tk.Button(janela, text="1", width=6, command=lambda: digitar(1))
botao_1.grid(row=4,column=0, padx=2, pady=2)

botao_2 = tk.Button(janela, text="2", width=6, command=lambda: digitar(2))
botao_2.grid(row=4,column=1, padx=2, pady=2)

botao_3 = tk.Button(janela, text="3", width=6, command=lambda: digitar(3))
botao_3.grid(row=4,column=2, padx=2, pady=2)

botao_4 = tk.Button(janela, text="4", width=6, command=lambda: digitar(4))
botao_4.grid(row=3,column=0, padx=2, pady=2)

botao_5 = tk.Button(janela, text="5", width=6, command=lambda: digitar(5))
botao_5.grid(row=3,column=1, padx=2, pady=2)

botao_6 = tk.Button(janela, text="6", width=6, command=lambda: digitar(6))
botao_6.grid(row=3,column=2, padx=2, pady=2)

botao_7 = tk.Button(janela, text="7", width=6, command=lambda: digitar(7))
botao_7.grid(row=2,column=0, padx=2, pady=2)

botao_8 = tk.Button(janela, text="8", width=6, command=lambda: digitar(8))
botao_8.grid(row=2,column=1, padx=2, pady=2)

botao_9 = tk.Button(janela, text="9", width=6, command=lambda: digitar(9))
botao_9.grid(row=2,column=2, padx=2, pady=2)


janela.mainloop()