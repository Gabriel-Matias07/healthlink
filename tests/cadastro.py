import sqlite3

def cadastrar_novo_usuario(nome, email, senha, confirmar_senha):
    """Cadastra um novo usuário no banco de dados.

    Args:
        nome (str): O nome do usuário.
        email (str): O email do usuário.
        senha (str): A senha do usuário.
        confirmar_senha (str): A confirmação da senha do usuário.

    Returns:
        bool: True se houver um erro durante o cadastro, False caso contrário.
    """

    # Validando informações:
    erro = False
    if nome:
        pass
    if "@" in email and ".com":
        pass
    if senha == confirmar_senha and len(senha) > 5:
        pass
    else:
        erro = True

    try:
        # Criando e se conectando ao banco de dados:
        banco = sqlite3.connect("data_user.db")  # Cria o arquivo data_user (caso não exista) do banco de dados para armazenar
        cursor = banco.cursor()  # Cria um objeto cursor para executar comandos SQL no banco de dados SQLite.

        cursor.execute("CREATE TABLE IF NOT EXISTS data_user (nome text, email text, senha text)")  # Cria uma tabela dentro do arquivo .db

        # Inserindo informações no banco de dados:
        cursor.execute(f"INSERT INTO data_user VALUES ('{nome}', '{email}', '{senha}')")  # Insere os arquivos na tabela

        banco.commit()  # Envia os arquivos
        banco.close()

    except sqlite3.Error as error:  # Criado excessão com try, caso dê erro, o except é inicializado
        print(error)
        erro = True
    return erro

# Realizando a introdução dos dados:
def introduzir_dados_usuarios():
    """Solicita informações do usuário para realizar o cadastro."""
    print("\n")
    print("----Olá, vamos realizar o seu cadastro no nosso sistema----\n")
    nome = input("Digite o seu nome: ")
    email = input("Digite o seu email: ")
    senha = input("Digite a sua senha: ")
    confirmar_senha = input("Confirme a sua senha: ")
    print("\n")
    
    # Chamando a função:
    if not cadastrar_novo_usuario(nome, email, senha, confirmar_senha):
        print("Cadastro realizado com sucesso!\n")
    else:
        print("Erro ao cadastrar!")