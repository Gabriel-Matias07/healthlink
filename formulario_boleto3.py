import sqlite3, os
from datetime import datetime

# Função para criar o banco de dados dos boletos
def tabela_boleto():
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'boletos.db')

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
    caminho_bd = os.path.join(diretorio_atual, 'boletos.db')

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
    print("Dados do boleto salvos com sucesso!")

# Função para garantir que o valor do boleto é positivo
def validar_valor(valor):
    try:
        valor_float = float(valor)
        return valor_float > 0
    except ValueError:
        return False

# Função principal para o cadastro
def main():
    tabela_boleto()
    print("== Formulário do Boleto ==")
    nome_cliente = input("Nome completo: ")
    cpf_cliente = input("CPF (somente números): ")
    while not validar_cpf(cpf_cliente):
        print("CPF inválido. Use o formato padrão somente com números.")
        cpf_cliente = input("CPF (somente números): ")

    valor_boleto = input("Valor do boleto: ")
    while not validar_valor(valor_boleto):
        print("Valor inválido. O valor deve ser positivo e apenas com números.")
        valor_boleto = input("Valor do boleto: ")

    vencimento_boleto = input("Data de vencimento (DD/MM/YYYY): ")
    while not validar_data(vencimento_boleto):
        print("Data de vencimento inválida. Use o formato DD/MM/YYYY.")
        vencimento_boleto = input("Data de vencimento (DD/MM/YYYY): ")

    salvar_boleto(nome_cliente, cpf_cliente, valor_boleto, vencimento_boleto)
    
if __name__ == "__main__":
    main()