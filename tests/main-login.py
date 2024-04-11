import login
email = input("Digite o seu email: ")
senha = input("Digite a sua senha: ")
print(login.receber_dados(email, senha))
login.validacao_login(email, senha)