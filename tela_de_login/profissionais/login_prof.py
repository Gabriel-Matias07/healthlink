import sqlite3
import senha_recovery

def login_profissional():
    email_user = input("Digite seu email: ")
    senha_user = input("Digite sua senha: ")
    
    if email_user:
        pass
    else:
        print("Email vazio")
        login_profissional()
    if "@" in email_user and ".com":
        pass
    else:
        print("Email inválido!")
        login_profissional()
    if len(senha_user) > 5:
        pass
    else:
        print("Senha muito curta!")
        login_profissional()
    
    try:
        banco = sqlite3.connect("data_user.db")
        cursor = banco.cursor()

        cursor.execute("SELECT email, senha FROM data_user WHERE email = ?", (email_user, ))
        resultado = cursor.fetchone()

        if resultado:
            email_bd, senha_bd = resultado
       
            if senha_user == senha_bd:
                print("Login bem-sucedido!")

                return 'Acesso Liberado'
            else:
                contador = 1
                while contador < 3:
                    print("Senha incorreta!")
                    senha_user = input("Digite novamente sua senha: ")
                    if senha_user == senha_bd:
                        print("Login bem-sucedido!")

                        return 'Acesso Liberado'
                    contador += 1
               
                senha_recovery.nova_senha(email_user)
        else:
            print("Email não encontrado. Verifique o email e tente novamente.")

        banco.close()
        
    except sqlite3.Error as error:
        print(error)