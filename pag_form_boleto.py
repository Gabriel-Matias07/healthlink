import sqlite3, os
from datetime import datetime
from login_utils import encerrar

# Função para criar o banco de dados dos boletos
def tabela_boleto():
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'pag_data_base/boletos.db')

    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS boleto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cpf TEXT,
            valor TEXT,
            vencimento TEXT
        )
    ''')

    conexao.commit()
    conexao.close()

# Função para inserir um novo boleto
def inserir_boleto(nome, cpf, valor, vencimento):  
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'pag_data_base/boletos.db')

    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()

    cursor.execute('''
        INSERT INTO boleto (nome, cpf, valor, vencimento)
        VALUES (?, ?, ?, ?)
    ''', (nome, cpf, valor, vencimento))

    conexao.commit()
    conexao.close()

# Função para validar a data
def validar_data(data):
    try:
        data_obj = datetime.strptime(data, '%d/%m/%Y')
        return data_obj >= datetime.now()
    except ValueError:
        return False

# Função de validação do cpf    
def validar_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    return True

# Função para salvar o boleto no banco se a data for válida
def salvar_boleto(nome, cpf, valor, vencimento):
    if not validar_data(vencimento):
        print("Data de vencimento inválida. Use o formato DD/MM/YYYY.")
        return
    
    inserir_boleto(nome, cpf, valor, vencimento)
    encerrar()
    print("\nDados do boleto salvos com sucesso!")
    print("Pagamento Realizado!")

# Função principal para o cadastro
def main(valor):
    tabela_boleto()
    print("== Formulário do Boleto ==")
    nome_cliente = input("Insira o seu nome novamente: ")
    cpf_cliente = input("CPF (somente números): ")
    while not validar_cpf(cpf_cliente):
        print("CPF inválido. Use o formato padrão somente com números.")
        cpf_cliente = input("CPF (somente números): ")

    valor_boleto = valor

    vencimento_boleto = input("Data de vencimento (DD/MM/YYYY): ")
    while not validar_data(vencimento_boleto):
        print("Data de vencimento inválida. Use o formato DD/MM/YYYY.")
        vencimento_boleto = input("Data de vencimento (DD/MM/YYYY): ")

    salvar_boleto(nome_cliente, cpf_cliente, valor_boleto, vencimento_boleto)
    
if __name__ == "__main__":
    main(0)