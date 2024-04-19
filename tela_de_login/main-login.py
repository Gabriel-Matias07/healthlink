import login
import cadastro

def main():
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