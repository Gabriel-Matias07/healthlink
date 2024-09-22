import sqlite3, menu_usuario3, agendamentos3

# Função para obter dados dos profissionais do banco de dados dados_profissionais.db
def obter_dados_profissionais():
    conn = sqlite3.connect('dados_profissionais.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT nome, email FROM dados_profissionais")
    profissionais = cursor.fetchall()
    
    conn.close()
    return profissionais

# Função para obter informações adicionais dos profissionais no banco informacoes_prof.db
def obter_informacoes_profissionais():
    conn = sqlite3.connect('informacoes_prof.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT telefone, estado, cidade, bairro, numeroCasa, horario FROM informacoes_prof")
    informacoes_profissionais = cursor.fetchall()
    
    conn.close()
    return informacoes_profissionais

# Função para mostrar informações detalhadas dos profissionais
def mostrar_informacoes_profissionais(informacoes_profissionais, profissionais):
    for i, info in enumerate(informacoes_profissionais):
        print(f"\nProfissional {i + 1}:")
        print(f"Nome: {profissionais[i][0]}")
        print(f"Email: {profissionais[i][1]}")
        print(f"Telefone: {info[0]}")
        print(f"Estado: {info[1]}")
        print(f"Cidade: {info[2]}")
        print(f"Bairro: {info[3]}")
        print(f"Número da Casa: {info[4]}")
        print(f"Horário: {info[5]}")

# Função para o usuário escolher um profissional
def escolher_profissional(informacoes_profissionais):
    for i, info in enumerate(informacoes_profissionais):
        print(f"{i + 1}. Profissional - {info[2]}, {info[1]}")  # Mostrando cidade e estado

    escolha = input("Escolha o número do profissional: ")
    
    try:
        escolha_index = int(escolha) - 1
        if 0 <= escolha_index < len(informacoes_profissionais):
            return informacoes_profissionais[escolha_index]
        else:
            print("Escolha inválida.")
            return None
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        return None

# Função simulando a tela de pagamento
def tela_pagamento(profissional):
    print(f"\nIniciando tela de pagamento para o profissional na cidade de {profissional[2]}, estado {profissional[1]}.")
    agendamentos3.criar_tabela_agendamentos()
    menu_usuario3.menu_principal()

# Função simulando a volta para o login
def voltar_login():
    print("\nVoltando para a tela de login...")

# Função para encerrar o programa
def encerrar_programa():
    print("\nEncerrando o programa. Até logo!")
    exit()

# Função principal que será chamada no main1.py
def menu_principal(nome_usuario, email_usuario):
    profissionais = obter_dados_profissionais()
    informacoes_profissionais = obter_informacoes_profissionais()
    
    profissional_escolhido = None  # Variável para armazenar o profissional escolhido
    
    while True:
        print("\n--- Menu Principal ---")
        print("1. Ver informações dos profissionais")
        print("2. Escolher um profissional")
        print("3. Ir para tela de pagamento")
        print("4. Voltar para o login")
        print("5. Encerrar o programa")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            mostrar_informacoes_profissionais(informacoes_profissionais, profissionais)
        elif escolha == "2":
            profissional_escolhido = escolher_profissional(informacoes_profissionais)
            if profissional_escolhido:
                nome_prof = profissionais[informacoes_profissionais.index(profissional_escolhido)][0]
                print(f"\nVocê escolheu o profissional: {nome_prof}")
        elif escolha == "3":
            if profissional_escolhido:
                tela_pagamento(profissional_escolhido)
            else:
                print("\nVocê precisa escolher um profissional antes de ir para a tela de pagamento.")
        elif escolha == "4":
            voltar_login()
            break
        elif escolha == "5":
            encerrar_programa()
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Função que será chamada pelo main1.py
def iniciar_menu_principal():
    dados_profissionais = obter_dados_profissionais()
    if dados_profissionais:
        nome_usuario = dados_profissionais[0][0]  # Nome do primeiro profissional
        email_usuario = dados_profissionais[0][1]  # Email do primeiro profissional
        menu_principal(nome_usuario, email_usuario)


