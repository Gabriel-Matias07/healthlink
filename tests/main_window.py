from tkinter import *
import main_login


janela = Tk()
janela.title('Login')

texto = Label(janela, text='Faça o seu login')
texto.grid(column=0, row=0, padx=25, pady=25)

botao = Button(janela, text='Executar', command=main)
botao.grid(column=0, row=1, padx=25, pady=25)

texto_resposta = Label(janela, text='')
texto_resposta.grid(column=0, row=2, padx=30, pady=30)















janela.mainloop()