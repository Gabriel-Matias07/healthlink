def menu_principal_usuario():
    print("Bem-vindo à tela de pagamentos, caro usuário.")
    print("Vamos prosseguir com o seu atendimento!")
    print("Insira seus dados bancários para prosseguir: ")
    nome = input("Digite o seu nome: ")
    num_conta = input("Número da conta: ")
    saldo = input("Saldo: ")
    return nome, num_conta, saldo