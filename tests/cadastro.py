import sqlite3

#Validando informações:
def cadastrar_novo_usuario(nome, email, senha, confirmar_senha):
    erro = False
    if not nome or not "@" in email or not ".com" in email or senha != confirmar_senha or len(senha) <= 5:
        erro = True
    else:
        try:
            banco = sqlite3.connect("data_user.db")
            cursor = banco.cursor()

            cursor.execute("CREATE TABLE IF NOT EXISTS data_user (nome text, email text, senha text)")
            cursor.execute("SELECT COUNT(*) AS existe_login FROM data_user WHERE email = ?", (email, ))
            existe_login = cursor.fetchone()[0]

            if existe_login > 0:
                print("Email já cadastrado! Insira um endereço de email não cadastrado.")
                erro = True
            else:
                cursor.execute(f"INSERT INTO data_user VALUES (?, ?, ?)", (nome, email, senha))
                banco.commit()
                banco.close()
        except sqlite3.Error as error:
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
        print("Erro ao cadastrar! Verifique os dados e tente novamente.")