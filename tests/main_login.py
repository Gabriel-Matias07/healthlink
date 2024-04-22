from tkinter import *
import login
import cadastro


def main():
    """Função principal do programa.

    Esta função exibe uma mensagem de boas-vindas ao usuário e permite que ele selecione
    entre profissiona ou cliente e realizar login, cadastrar um novo usuário ou encerrar o programa.

    Returns:
        None
    """
    print("\n")
    print("----------------------------------Bem vindo ao HealthLink---------------------------------\n")
    print("-------------MENU-------------\n")
    print("----Escolha a opção desejada----\n")
    print("--- Login (Digite 1)")
    print("--- Cadastro (Digite 2)")
    print("--- Encerrar (Digite 0)\n")
    print("------------------------------")
    
    resposta_login_cadas_encer = input("R = ")
    print("\n")
    
    if resposta_login_cadas_encer == "1":
        login.login_usuario()
    if resposta_login_cadas_encer == "2":
        cadastro.introduzir_dados_usuarios()
    if resposta_login_cadas_encer == "0":
        print("----Fim----")

    return None

if __name__ == "__main__":
    main()