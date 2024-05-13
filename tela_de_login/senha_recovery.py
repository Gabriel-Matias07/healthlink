import login
import sqlite3
import time

""" def recovery(email_recovery):
    print("Esqueceu sua senha? Digite 1 para prosseguir com a recuperação ou 2 para retornar ao login.")
    senha_recovery = input()
    print("Digite 1 para Usuário ou 2 para Profissional: ")
    prof_user_recovery = input()
    if senha_recovery == '1':
        if prof_user_recovery == '1':
            print(f"Ótimo, enviamos um link de recuperação para o email {email_recovery}, cadastrado como usuário.")
            exit()
        elif prof_user_recovery == '2':
            print(f"Ótimo, enviamos um link de recuperação para o email {email_recovery}, cadastrado como profissional.")
            exit()
    elif senha_recovery == '2':
        login.login_usuario()
    else:
        print("Entrada inválida!")
        exit()
 """
def nova_senha(email_recovery):
    print("Esqueceu sua senha? Digite 1 para prosseguir com a recuperação ou 2 para retornar ao login.")
    resultado = str(input())
    if resultado == '1':
        print("Digite 1 para usuário ou 2 para profissional: ")
        user_or_prof = str(input())
        if user_or_prof == '1':
            inserir_nova_senha_user(email_recovery)
        elif resultado == '2':
            """ inserir_nova_senha_prof(email_recovery) """
            pass
    elif resultado == '2':
        login.login_usuario()

#Insere a nova senha no banco de dados  
def inserir_nova_senha_user(email_recovery):
    erro = False
    print("Digite sua nova senha: ")
    nova_senha = input()
    if len(nova_senha) >= 5:
        try:
            banco = sqlite3.connect("data_user.db")
            cursor = banco.cursor()

            cursor.execute("UPDATE data_user SET senha = ? WHERE email = ?", (nova_senha, email_recovery, ))
            banco.commit()
            banco.close()
            
            print("Finalizando processo...")
            time.sleep(3)
            print("Inserindo dados...")
            time.sleep(3)
            print("Senha alterada com sucesso!")

            exit()
        except sqlite3.Error as error:
            error = True
            print(error)

            exit()
    else:
        erro = True
        print("Senha muito curta!")

    return erro