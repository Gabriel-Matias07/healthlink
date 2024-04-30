import sqlite3

#Validando informações:
def cadastrar_novo_usuario(nome, email, senha, confirmar_senha):
    erro = False
    if nome:
        pass
    if "@" in email and ".com":
        pass
    if senha == confirmar_senha and len(senha) > 5:
        pass
    else:
        erro = True

#Criando e se conectando ao banco de dados:
    try:
        banco = sqlite3.connect("data_user.db") #Cria o arquivo data_user (caso não exista) do banco de dados para armazenar
        cursor = banco.cursor() #Cria um objeto cursor para executar comandos SQL no banco de dados SQLite.


        cursor.execute("CREATE TABLE IF NOT EXISTS data_user (nome text, email text, senha text)") #Cria uma tabela dentro do arquivo .db

#Inserindo informações no bando de dados:        
        cursor.execute(f"INSERT INTO data_user VALUES ('{nome}', '{email}', '{senha}')") #Insere os arquivos na tabela

        banco.commit() #Envia os arquivos
        banco.close()

    except sqlite3.Error as error: #Criado excessão com try, caso dê erro, o except é inicializado
        print(error)
        erro = True
    return erro

#Realizando a introdução dos dados:
def introduzir_dados_usuarios():
    print("\n")
    print("----Olá, vamos realizar o seu cadastro no nosso sistema----\n")
    nome = input("Digite o seu nome: ")
    email = input("Digite o seu email: ")
    senha = input("Digite a sua senha: ")
    confirmar_senha = input("Confirme a sua senha: ")
    print("\n")
    
    #Chamando a função:
    if not cadastrar_novo_usuario(nome, email, senha, confirmar_senha):
        print("Cadastro realizado com sucesso!\n")
    else:
        print("Erro ao cadastrar!")