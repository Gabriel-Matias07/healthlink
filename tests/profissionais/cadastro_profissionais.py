import sqlite3

#Validando informações:
def cadastrar_novo_profissional(nome, email, senha, confirmar_senha):
    erro = False
    if not nome or not "@" in email or not ".com" in email or senha != confirmar_senha or len(senha) <= 5:
        erro = True
    else:
        try:
            banco = sqlite3.connect("data_profissional.db") #Cria o arquivo data_profissional (caso não exista) do banco de dados para armazenar
            cursor = banco.cursor() #Cria um objeto cursor para executar comandos SQL no banco de dados SQLite.

            cursor.execute("CREATE TABLE IF NOT EXISTS data_profissional (nome text, email text, senha text)")
            cursor.execute("SELECT COUNT(*) AS existe_login FROM data_profissional WHERE email = ?", (email, ))
            existe_login = cursor.fetchone()[0]

            if existe_login > 0:
                print("Email já cadastrado! Insira um endereço de email não cadastrado.")
                erro = True
            else:
                cursor.execute(f"INSERT INTO data_profissional VALUES (?, ?, ?)", (nome, email, senha)) #Insere os valores na tabela
                banco.commit() #Envia os arquivos
                banco.close()
        except sqlite3.Error as error: #Criado excessão com try, caso dê erro, o except é inicializado
            print(error)
            erro = True
    return erro

#Realizando a introdução dos dados:
def introduzir_dados_profissional():
    print("\n")
    print("----Olá, vamos realizar o seu cadastro no nosso sistema----\n")
    nome = input("Digite o seu nome: ")
    email = input("Digite o seu email: ")
    senha = input("Digite a sua senha: ")
    confirmar_senha = input("Confirme a sua senha: ")
    print("\n")
    
    #Chamando a função:
    if not cadastrar_novo_profissional(nome, email, senha, confirmar_senha):
        print("Cadastro realizado com sucesso!\n")
    else:
        print("Erro ao cadastrar! Verifique os dados e tente novamente.")