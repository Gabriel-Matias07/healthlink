import sqlite3
import random
import string

def gerar_email():
    """Gera um email aleatório."""
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']
    name = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10)))
    domain = random.choice(domains)
    return f"{name}@{domain}"

def gerar_senha():
    """Gera uma senha aleatória."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(8, 12)))

def inserir_dados_aleatorios(quantidade):
    """Insere uma quantidade especificada de dados aleatórios no banco de dados."""
    try:
        banco = sqlite3.connect("data_user.db")
        cursor = banco.cursor()

        for _ in range(quantidade):
            nome = ''.join(random.choices(string.ascii_uppercase, k=random.randint(5, 10)))
            email = gerar_email()
            senha = gerar_senha()

            cursor.execute("INSERT INTO data_user VALUES (?, ?, ?)", (nome, email, senha))

        banco.commit()
        banco.close()
        print(f"{quantidade} registros inseridos com sucesso!")
    except sqlite3.Error as error:
        print(error)

# Insere 100 registros aleatórios
inserir_dados_aleatorios(100)