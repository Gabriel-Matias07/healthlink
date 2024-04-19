import login
import cadastro

def main():
    """Função principal do programa.

    Esta função exibe uma mensagem de boas-vindas ao usuário e permite que ele selecione
    entre realizar login, cadastrar um novo usuário ou encerrar o programa.

    Returns:
        None
    """
    print("----Bem vindo ao HealthLink----")
    print("----Selecione 1 para login, 2 para cadastro ou 0 para encerrar----")

    resposta = input()

    if resposta == '1':
        login.login_usuario()
    elif resposta == '2':
        cadastro.introduzir_dados_usuarios()
    elif resposta == '0':
        print('----Fim----')

if __name__ == "__main__":
    main()