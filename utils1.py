import sys,time,os

#Módulo para funções utilitárias que podem ser usadas em várias partes do programa

#Função que imprime mensagem caso sucesso no cadastro
def msg_sucesso():
    print("\n")
    print("Cadastro realizado com sucesso. ")
    return None

#Função que limpa o terminal ao ser chamada
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
#Função que limpa o terminal e encerra o programa
def encerrar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Programa encerrado. ')
    return None

#Função para animação de inserção de dados
def carregamento():
    time.sleep(1)
    print("Abrindo o Banco de Dados...")
    time.sleep(2)
    print("Inserindo Informações...")
    time.sleep(2)
    return None

#Escreve o texto de apresentação com animação corrida
def escrevendo_texto(texto, atraso):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(atraso)
    print()

#Retorna qual opção foi selecionada na tela inicial de login, auxiliando as outros telas a se adaptarem
def repassar_user_ou_prof(info):
    return info

#Funções que retornam o nome completo do usuário para serem chamadas em outros módulos
def passar_nome_user(nome):
    return nome
def passar_nome_prof(nome):
    return nome

#Retorna uma lista contento as preferências do usuário e profissional
def passar_preferencias_contratacao_user(list):
    return list

#Retorna uma lista contendo telefone, estado, cidade, bairro, telefone, numero_casa, horario
def passar_informacoes_profissional(list):
    return list