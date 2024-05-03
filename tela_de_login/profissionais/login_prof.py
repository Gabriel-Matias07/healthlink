import sqlite3
import senha_recovery

def login_profissional(contador = 0):
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
        banco = sqlite3.connect("data_profissional.db")
        cursor = banco.cursor()

        cursor.execute("SELECT email, senha FROM data_profissional WHERE email = ?", (email_user, ))
        resultado = cursor.fetchone()

        if resultado:
            email_bd, senha_bd = resultado
       
            if senha_user == senha_bd:
                print("Login bem-sucedido!")
            else:
                contador += 1
                if contador == 3:
                    contador = 0
                    senha_recovery.recovery(email_user)
                else:
                    pass
                print("Senha incorreta. Tente novamente.")
                login_profissional(contador)
        else:
            print("Email não encontrado. Verifique o email e tente novamente.")

        banco.close()
        
    except sqlite3.Error as error:
        print(error)

    return 'Acesso Liberado'