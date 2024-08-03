import time
import sys
import sqlite3
import os

#----------------------------------------------------------FUNÇÕES GENÉRICAS---------------------------------------------------------------
#Ao longo do programa, observo funções que posso generalizar para evitar ambiguidade


#Função que imprime mensagem caso sucesso no cadastro
def msg_sucesso():
    print("\n")
    print("Cadastro realizado com sucesso. ")
    return None

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

#----------------------------------------------------------MÓDULO DE APRESENTAÇÃO----------------------------------------------------------

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

    texto = "----O HealthLink é uma plataforma inovadora voltada para a área da saúde, desenvolvida para facilitar a comunicação direta e a contratação de profissionais de saúde.\n Nossa missão é democratizar o acesso aos serviços de saúde, conectando pacientes e profissionais de maneira eficiente e segura.----\n"
    escrevendo_texto(texto, atraso=0.005)

#----------------------------------------------------------MÓDULO DE ESCOLHAS-------------------------------------------------------------

#Função para escolher entre prestador de serviços, cliente ou encerrar programa
def escolher_opcao():
    escolha = input("Digite 1 para Usuário, 2 para Profissional ou 0 para encerrar: \n")
    if escolha == '1':
        retorno = "usuario"
        return usuario(), redirecionar(retorno)
    elif escolha == '2':
        retorno = "profissional"
        return profissional(), redirecionar(retorno)
    elif escolha == '0':
        return encerrar()
    else:
        print("Resposta inválida. ")
        return escolher_opcao()
    
#----------------------------------------------------------MÓDULO GERAL DO USUÁRIO----------------------------------------------------------

#Função que permite usuário escolher entre login, cadastro no sistema ou encerrar programa
def usuario():
    print("Opção 'Usuário' selecionada. \n")
    escolha = input("Selecione 1 para login, 2 para cadastro ou 0 para encerrar: ")
    if escolha == '1':
        return login_usuario()
    elif escolha == '2':
        return cadastro_usuario()
    elif escolha == '0':
        return encerrar()
    else:
        print("Resposta Inválida. ")
        return usuario()

#Função mãe de cadastro, ela chama e passa os parâmetros para as outras funções
def cadastro_usuario():
    nome = cadastro_nome()
    email = cadastro_email()
    senha = cadastro_senha()
    confirma_senha(senha)
    carregamento()
    inserir_bd_usuario(nome, email, senha)
    msg_sucesso()

def cadastro_nome():
    nome = input("Digite o seu nome: ")
    if not nome:
        print("Nome Inválido")
        return cadastro_nome()
    else:
        return nome

def cadastro_email():
    email = input("Digite o seu email: ")
    if not '@' in email or not '.com' in email:
        print("Um email válido deve conter '@' e '.com'. ")
        return cadastro_email()
    else:
        return email

def cadastro_senha():
    senha = input("Digite a sua senha: ")
    if len(senha) <= 5:
        print("Uma senha válida precisa ter mais de 5 caracteres. ")
        return cadastro_senha()
    else:
        return senha

def confirma_senha(senha):
    conf_senha = input("Confirme sua senha: ")
    if senha != conf_senha:
        print("As senhas são diferentes. ")
        return confirma_senha(senha)
    else:
        return None

#Função que insere os dados do cliente no banco de dados
def inserir_bd_usuario(nome, email, senha):
    erro = False
    try:
        banco = sqlite3.connect("dados_usuarios.db") #Conecta o banco de dados
        cursor = banco.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS dados_usuarios (nome text, email text, senha text)") #Cria o banco caso não exista
        cursor.execute("SELECT COUNT(*) AS existe_login FROM dados_usuarios WHERE email = ?", (email, )) #Verifica se o email já existe no banco
        existe_login = cursor.fetchone()[0]

        if existe_login > 0:
            print("Email já cadastrado. Insira um endereço de email não cadastrado. ")
            erro = True
        else:
            cursor.execute(f"INSERT INTO dados_usuarios VALUES (?, ?, ?)", (nome, email, senha)) #Insere os valores no banco
            banco.commit()
            banco.close()

    except sqlite3.Error as error:
        print(error)
        erro = True
    return erro

#Função para verificar se o login existe e logar no sistema
def login_usuario():
    email_login = input("Digite seu email: ")
    senha_login = input("Digite sua senha: ")

    if not '@' in email_login or not '.com' in email_login:
        print("Um email válido deve conter '@' e '.com'")
        return login_usuario()
    else:
        pass
    if len(senha_login) <= 5:
        print("Uma senha válida precisa ter mais de 5 caracteres. ")
        return login_usuario()
    try:
        banco = sqlite3.connect("dados_usuarios.db")
        cursor = banco.cursor()
        cursor.execute("SELECT senha FROM dados_usuarios WHERE email = ?", (email_login,)) #Verifica a coluna senha onde email condiz ao parêmetro
        resultado = cursor.fetchone() #Retorna uma tupla contendo o valor da coluna senha

        if resultado:
            senha_salva = resultado[0]
            if senha_login == senha_salva:
                print("Login bem-sucedido.")
            else:
                print("Senha incorreta.")
                resposta = input("Esqueceu sua senha? Digite 1 para recuperar ou 2 para tentar novamente: ")
                if resposta == '1':
                    return recuperar_senha_usuario(email_login)
                elif resposta == '2':
                    return login_usuario()
                else:
                    print("Valor inválido.")
                    return login_usuario()
        else:
            print("Email não encontrado.")
            return login_usuario()
    except sqlite3.Error as error:
        print(error)

#Função que recupera senha do usuário para email especificado        
def recuperar_senha_usuario(email_login):
    email_base = email_login
    nova_senha =  input(f"Digita uma nova senha para o email '{email_login}': ")
    return inserir_nova_senha_usuario(nova_senha, email_base)

#Função que insere a nova senha no banco de dados
def inserir_nova_senha_usuario(nova_senha, email_base):
    try:
        banco = sqlite3.connect("dados_usuarios.db")
        cursor = banco.cursor()
        cursor.execute("UPDATE dados_usuarios SET senha = ? WHERE email = ?", (nova_senha, email_base)) #Atualiza a senha para o email de parâmetro
        banco.commit()
        banco.close()
        time.sleep(2)
        print("Atualizando senha...")
        time.sleep(2)
        print("Senha atualizada com sucesso.")
        time.sleep(0.5)
        print("Retornando para o login...")
        time.sleep(2)
        #os.system('cls' if os.name == 'nt' else 'clear')
        return login_usuario()
    except sqlite3.Error as error:
        print(error)

#----------------------------------------------------------MÓDULO GERAL DO PROFISSIONAL----------------------------------------------------------
# Módulo idêntico ao usuário, mas que mainupula dados do profissional


#Função que permite profissional escolher entre login, cadastro no sistema ou encerrar programa
def profissional():
    print("Opção 'Profissional' selecionada. \n")
    escolha = input("Selecione 1 para login, 2 para cadastro ou 0 para encerrar: ")
    if escolha == '1':
        login_profissional()
    elif escolha == '2':
        cadastro_profissional()
    elif escolha == '0':
        encerrar()
    else:
        print("Resposta inválida. ")
        return profissional()

#Função mãe de cadastro, ela chama e passa os parâmetros para as outras funções (profissional)
def cadastro_profissional():
    nome = cadastro_nome()
    email = cadastro_email()
    senha = cadastro_senha()
    confirma_senha(senha)
    carregamento()
    inserir_bd_profissional(nome, email, senha)
    msg_sucesso()

def cadastro_nome():
    nome = input("Digite o seu nome: ")
    if not nome:
        print("Nome inválido. ")
        return cadastro_nome()
    else:
        return nome

def cadastro_email():
    email = input("Digite o seu email: ")
    if not '@' in email or not '.com' in email:
        print("Um email válido deve conter '@' e '.com'")
        return cadastro_email()
    else:
        return email

def cadastro_senha():
    senha = input("Digite a sua senha: ")
    if len(senha) <= 5:
        print("Uma senha válida precisa ter mais de 5 caracteres. ")
        return cadastro_senha()
    else:
        return senha

def confirma_senha(senha):
    conf_senha = input("Confirme sua senha: ")
    if senha != conf_senha:
        print("As senhas são diferentes. ")
        return confirma_senha(senha)
    else:
        return None

#Função que insere os dados do profissional no banco de dados
def inserir_bd_profissional(nome, email, senha):
    erro = False
    try:
        banco = sqlite3.connect("dados_profissionais.db") #Conecta o banco de dados
        cursor = banco.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS dados_profissionais (nome text, email text, senha text)") #Cria o banco caso não exista
        cursor.execute("SELECT COUNT(*) AS existe_login FROM dados_profissionais WHERE email = ?", (email, )) #Verifica se o email já existe no banco
        existe_login = cursor.fetchone()[0]

        if existe_login > 0:
            print("Email já cadastrado. Insira um endereço de email não cadastrado. ")
            erro = True
        else:
            cursor.execute(f"INSERT INTO dados_profissionais VALUES (?, ?, ?)", (nome, email, senha)) #Insere os valores no banco
            banco.commit()
            banco.close()

    except sqlite3.Error as error:
        print(error)
        erro = True
    return erro

#Função para verificar se o login existe e logar no sistema
def login_profissional():
    email_login = input("Digite seu email: ")
    senha_login = input("Digite sua senha: ")

    if not '@' in email_login or not '.com' in email_login:
        print("Um email válido deve conter '@' e '.com'")
        return login_profissional()
    else:
        pass
    if len(senha_login) <= 5:
        print("Uma senha válida precisa ter mais de 5 caracteres. ")
        return login_profissional()
    try:
        banco = sqlite3.connect("dados_profissionais.db")
        cursor = banco.cursor()
        cursor.execute("SELECT senha FROM dados_profissionais WHERE email = ?", (email_login,)) #Verifica a coluna senha onde email condiz ao parêmetro
        resultado = cursor.fetchone() #Retorna uma tupla contendo o valor da coluna senha

        if resultado:
            senha_salva = resultado[0]
            if senha_login == senha_salva:
                print("Login bem-sucedido. ")
            else:
                print("Senha incorreta. ")
                resposta = input("Esqueceu sua senha? Digite 1 para recuperar ou 2 para tentar novamente: ")
                if resposta == '1':
                    return recuperar_senha_profissional(email_login)
                elif resposta == '2':
                    return login_profissional()
                else:
                    print("Valor inválido.")
                    return login_profissional()
        else:
            print("Email não encontrado.")
            return login_profissional()
    except sqlite3.Error as error:
        print(error)

#Função que recupera senha do usuário para email especificado        
def recuperar_senha_profissional(email_login):
    email_base = email_login
    nova_senha =  input(f"Digita uma nova senha para o email '{email_login}': ")
    inserir_nova_senha_profissional(nova_senha, email_base)

#Função que insere a nova senha no banco de dados
def inserir_nova_senha_profissional(nova_senha, email_base):
    try:
        banco = sqlite3.connect("dados_profissionais.db")
        cursor = banco.cursor()
        cursor.execute("UPDATE dados_profissionais SET senha = ? WHERE email = ?", (nova_senha, email_base)) #Atualiza a senha para o email de parâmetro
        banco.commit()
        banco.close()
        time.sleep(2)
        print("Atualizando senha...")
        time.sleep(2)
        print("Senha atualizada com sucesso. ")
        time.sleep(0.5)
        print("Retornando para o login...")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        return login_profissional()
    except sqlite3.Error as error:
        print(error)

# Função que armazena e retorna valores para uso em outro módulos
def usuario_ou_profissional(retorno):
    return redirecionar(retorno)

#--------------------------------------------------------MÓDULO GERAL DE CADASTRO DE INFORMAÇÕES--------------------------------------------------------

#Função que recebe qual valor e redireciona corretamente
def redirecionar(retorno):
    dado_retornado = retorno
    usuario = "usuario"
    profissional = "profissional"   
    if dado_retornado == usuario:
        return form_usuario(dado_retornado)
    elif dado_retornado == profissional:
        return form_profissional(dado_retornado)
    else:
        print(f"Retorno inesperado: {dado_retornado}")

#Função de formulário do usuário
def form_usuario(dado_retornado):
    print(f"Detectamos que você se cadastrou na nossa plataforma como {dado_retornado}. Iremos precisar de algumas informações para darmos prosseguimento.\n ")
    print("Informações pessoais.\n ")
    informacoes_pessoais = []
    endereco = []
    preferencia_user = []

    nome_completo = input("Nome completo: ")
    telefone = input("Telefone: ")
    print("Endereço completo.\n ")
    estado = input("Estado: ")
    cidade = input("Cidade: ")
    bairro = input("Bairro: ")
    numero_casa = input("Número da casa: ")

    #Adicionando valores nas listas
    informacoes_pessoais.append(nome_completo)
    informacoes_pessoais.append(telefone)
    endereco.append(estado)
    endereco.append(cidade)
    endereco.append(bairro)
    endereco.append(numero_casa)

    #Percorre uma lista pré-definida de opções, imprime e recebe da entrada padrão o valor escolhido, inserindo em uma lista
    print("Preferência de contratação.\n ")
    preferencias_contratacao_user = ['Médico', 'Enfermeiro', 'Fisioterapeuta']
    for i in range(len(preferencias_contratacao_user)):
        print(f"{i + 1} - {preferencias_contratacao_user[i]}" )
    print("\n")
    resposta = int(input("Selecione sua prefência: "))
    for i in range(len(preferencias_contratacao_user)):
        resposta = int(resposta)
        if resposta == i:
            add = preferencias_contratacao_user[i]
            print(add)
            preferencia_user.append(add)
    print(preferencia_user)

    return salvar_form_usuario(informacoes_pessoais, endereco)

#Função que armazena as informações permanentemente
def salvar_form_usuario(informacoes_pessoais, endereco):
    return None

def form_profissional():
    print("Em breve")

apresentacao()
escolher_opcao()