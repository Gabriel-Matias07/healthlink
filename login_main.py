import sys,time
import login_user, login_profissionais, login_utils, home_main

#Módulo que vai chamar as funções principais de outros módulos

#Função que apresenta um resumo do programa
def apresentacao():
    print("\n")
    print("----Bem Vindo ao HealthLink----\n")

    #Escreve o texto de apresentação com animação corrida
    def escrevendo_texto(texto, atraso):
        for char in texto:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(atraso)
        print()

    texto = "O HealthLink é uma plataforma inovadora voltada para a área da saúde, desenvolvida para facilitar a comunicação direta e a contratação de profissionais de saúde.\nNossa missão é democratizar o acesso aos serviços de saúde, conectando pacientes e profissionais de maneira eficiente e segura.\n"
    escrevendo_texto(texto, atraso=0.005)

#Função para escolher entre prestador de serviços (profissiona), cliente (usuário) ou encerrar programa
def escolher_opcao():
    escolha = input("Digite 1 para Usuário, 2 para Profissional ou 0 para encerrar: ")
    print("\n")
    if escolha == '1':
        retorno = "usuário"
        login_utils.repassar_user_ou_prof(retorno)
        return login_user.usuario(retorno)
    elif escolha == '2':
        retorno = "profissional"
        login_utils.repassar_user_ou_prof(retorno)
        return login_profissionais.profissional(retorno)
    elif escolha == '0':
        return login_utils.encerrar()
    else:
        print("Resposta inválida. ")
        return escolher_opcao()

apresentacao()
escolher_opcao()
def chamar_modulo2():
        return home_main.iniciar_menu_principal()

verdade = True

if verdade:
    chamar_modulo2()
else:
    login_utils.clear()
    login_utils.msg_sucesso()