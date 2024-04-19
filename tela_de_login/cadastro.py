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
        banco = sqlite3.connect("data_user.db") #Cria o arquivo data_user do banco de dados para armazenar
        cursor = banco.cursor() #Cria um objeto cursor para executar comandos SQL no banco de dados SQLite.


        cursor.execute("CREATE TABLE IF NOT EXISTS data_user (nome text, email text, senha text)") #Cria uma tabela dentro do arquivo .db

#Inserindo informações no bando de dados:        
        cursor.execute(f"INSERT INTO data_user VALUES ('{nome}', '{email}', '{senha}')") #Insere os arquivos na tabela

        banco.commit() #Envia os arquivo
        banco.close()

    except sqlite3.Error as error: #Criado excessão com try, caso dê erro, o except é inicializado
        print(error)
        erro = True
    return erro

#Chamando a função para testes:
if not cadastrar_novo_usuario("Gabriel", "gabrielpereira9036@gmail.com", "123456789", "123456789"):
    print("Cadastro realizado com sucesso!")
else:
    print("Erro ao cadastrar!")