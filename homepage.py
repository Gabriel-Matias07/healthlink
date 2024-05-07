import math

RESET = "\033[0;0m"
RED  = "\033[1;31m"

def apresentacao():
    print("""    
Bem-vindos a HealthLink✝️!!

Aqui iremos garantir um serviço de qualidade
uma ótima estadia no nosso sistema.

Esperamos que gostem ❤
    """)


def idenficacao_de_uso():

    print(""""""
"""--------------------------------------------------------------"""
+ RED + """
Para ajudarmos da melhor forma precisamos saber o que deseja:"""
+RESET+"""
--------------------------------------------------------------
======================= """+RED+"""HealthLink✝️"""+RESET+""" ============================
| ["""+RED+"""1"""+RESET+"""] Fazer um novo cadastro como cliente na HealthLink✝️                    |
| ["""+RED+"""2"""+RESET+"""] Fazer um novo cadastro Como prestador de serviço✝️                    |
| ["""+RED+"""3"""+RESET+"""] Sair do sistema✝️                                       |
--------------------------------------------------------------""") 

    escolha = int(input("O que deseja: "))
    def sair_do_sistema():
        print("Saindo do sistema...")

    match escolha:
        case 1:
            print("INDISPONIVEL")
        case 2:
            print("INDISPONIVEL")
        case 3:
            sair_do_sistema()

    
apresentacao()
idenficacao_de_uso()

