import login

def recovery(email_recovery):
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