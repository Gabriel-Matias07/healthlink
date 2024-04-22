import sqlite3

def login_usuario(tipo_usuario):
    """Realiza o processo de login do usuário."""
    email_user = input("Digite seu email: ")
    senha_user = input("Digite sua senha: ")
    
    if email_user:
        pass
    else:
        print("Email vazio")
        login_usuario(tipo_usuario)
    if "@" in email_user and ".com":
        pass
    else:
        print("Email inválido!")
        login_usuario(tipo_usuario)
    if len(senha_user) > 5:
        pass
    else:
        print("Senha muito curta!")
        login_usuario(tipo_usuario)
    
    try:
        if tipo_usuario == 'Cliente':
            # Conectando ao banco de dados do cliente:
            banco = sqlite3.connect("data_user_cliente.db")
            cursor = banco.cursor()

            cursor.execute("SELECT email, senha FROM data_user_cliente WHERE email = ?", (email_user,))
            resultado = cursor.fetchone()

            if resultado:
                email_bd, senha_bd = resultado
        
                if senha_user == senha_bd:
                    print("\n")
                    print("Login bem-sucedido!\n")
                else:
                    print("Senha incorreta. Tente novamente.")
            else:
                print("Email não encontrado. Verifique o email e tente novamente.")

            banco.close()
        else:
            # Conectando ao banco de dados do profissional:
            banco = sqlite3.connect("data_user_profissional.db")
            cursor = banco.cursor()

            cursor.execute("SELECT email, senha FROM data_user_profissional WHERE email = ?", (email_user,))
            resultado = cursor.fetchone()

            if resultado:
                email_bd, senha_bd = resultado
        
                if senha_user == senha_bd:
                    print("\n")
                    print("Login bem-sucedido!\n")
                else:
                    print("Senha incorreta. Tente novamente.")
            else:
                print("Email não encontrado. Verifique o email e tente novamente.")

            banco.close()
    except sqlite3.Error as error:
        print(error)
