import login
import cadastro
from profissionais import login_prof
from profissionais import cadastro_profissionais

def main():
    print("----Bem vindo ao HealthLink----")
    print("----Digite 1 para Usuário, 2 para Profissional ou 0 para encerrar----")
    user_or_prof = input()
    if user_or_prof == '1':
        print("Opção 'Usuário' selecionada! \n")
        print("----Selecione 1 para login, 2 para cadastro ou 0 para encerrar----")
        resposta = input()
        if resposta == '1':
            login.login_usuario()
        elif resposta == '2':
            cadastro.introduzir_dados_usuarios()
        elif resposta == '0':
            print('----Fim----')
        else:
            print("Resposta inválida")
            return None
    elif user_or_prof == '2':
        print("Opção 'Profissional' selecionada! \n")
        print("----Selecione 1 para login, 2 para cadastro ou 0 para encerrar----")
        resposta = input()
        if resposta == '1':
            login_prof.login_profissional()
        elif resposta == '2':
            cadastro_profissionais.introduzir_dados_profissional()
        elif resposta == '0':
            print('----Fim----')
        else:
            print("Resposta inválida")
            return None
        
if __name__ == "__main__":
    main()