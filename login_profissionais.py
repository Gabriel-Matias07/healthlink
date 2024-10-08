#Módulo para funções relacionadas ao profissional

import pwinput
import login_utils, login_db_utils, login_redirect

#Função que permite profissional escolher entre login, cadastro no sistema ou encerrar programa
def profissional(retorno):
    print("Opção 'Profissional' selecionada. \n")
    escolha = input("Selecione 1 para login, 2 para cadastro ou 0 para encerrar: ")
    if escolha == '1':
        print(retorno)
        return login_db_utils.login_profissional()
    elif escolha == '2':
        cadastro_profissional(), login_redirect.redirecionar(retorno)
    elif escolha == '0':
        login_utils.encerrar()
    else:
        print("Resposta inválida. ")
        return profissional()
    
#Função mãe de cadastro, ela chama e passa os parâmetros para as outras funções (profissional)
def cadastro_profissional():
    nome = cadastro_nome()
    email = cadastro_email()
    senha = cadastro_senha()
    confirma_senha(senha)
    login_utils.carregamento()
    login_db_utils.inserir_bd_profissional(nome, email, senha)
    login_utils.msg_sucesso()

def cadastro_nome():
    nome = input("Digite o seu nome completo: ")
    if not nome:
        print("Nome Inválido")
        return cadastro_nome()
    else:
        login_utils.passar_nome_prof(nome)
        return nome

def cadastro_email():
    email = input("Digite o seu email: ")
    if not '@' in email or not '.com' in email:
        print("Um email válido deve conter '@' e '.com'")
        return cadastro_email()
    else:
        return email

def cadastro_senha():
    senha = pwinput.pwinput(prompt = 'Digite a sua senha: ')
    if len(senha) <= 5:
        print("Uma senha válida precisa ter mais de 5 caracteres. ")
        return cadastro_senha()
    else:
        return senha

def confirma_senha(senha):
    conf_senha = pwinput.pwinput(prompt = 'Confirme sua senha: ')
    if senha != conf_senha:
        print("As senhas são diferentes. ")
        return confirma_senha(senha)
    else:
        return None

#Função que recupera senha do usuário para email especificado
def recuperar_senha_profissional(email_login):
    email_base = email_login
    nova_senha = pwinput.pwinput(prompt = f'Digita uma nova senha para o email {email_login}: ')
    return login_db_utils.inserir_nova_senha_profissional(nova_senha, email_base)      

def form_profissional(dado_retornado):
    print(f"Detectamos que você se cadastrou na nossa plataforma como {dado_retornado}. Iremos precisar de algumas informações para darmos prosseguimento.\n ")
    informacoes_pessoais = []
    preferencia_prof = [] 
    
    telefone = input("Telefone: ")
    estado = input("Estado: ")
    cidade = input("Cidade: ")
    bairro = input("Bairro: ")
    numero_casa = input("Número da casa: ")
    horario = input("Digite o horário no formato 00:00h: ")

    informacoes_pessoais.append(telefone)
    informacoes_pessoais.append(estado)
    informacoes_pessoais.append(cidade)
    informacoes_pessoais.append(bairro)
    informacoes_pessoais.append(numero_casa)
    informacoes_pessoais.append(horario)

    login_utils.passar_informacoes_profissional(informacoes_pessoais)
    login_db_utils.salvar_form_profissional(telefone, estado, cidade, bairro, numero_casa, horario)