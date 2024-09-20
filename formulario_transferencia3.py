import sqlite3, os
from datetime import datetime
from utils1 import passar_nome_user, encerrar

#Função para criar o banco de dados das transferências
def criar_tabela():
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'transferencias.db')
    
    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS transferencia (
                        id INTEGER PRIMARY KEY,
                        nome TEXT,
                        cpf TEXT,
                        banco TEXT, 
                        agencia TEXT, 
                        conta TEXT, 
                        valor TEXT,
                        data TEXT)''')
    conexao.commit()
    conexao.close()

#Função para inserir os dados no banco
def inserir_dados(nome, cpf, banco, agencia, conta, valor, data):
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'transferencias.db')
    
    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO transferencia (nome, cpf, banco, agencia, conta, valor, data)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''', (nome, cpf, banco, agencia, conta, valor, data))
    conexao.commit()
    id = cursor.lastrowid
    conexao.close()
    return id

#Função para verificação de nome e conta
def verificacao(nome, conta):
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'transferencias.db')
    
    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM transferencia WHERE nome = ? AND conta = ?''', (nome, conta))
    resultado = cursor.fetchone()
    conexao.close()
    return resultado is not None

import os

def emissao_comprovante(id, nome, cpf, banco, agencia, conta, valor_servico, data):
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    pasta_comprovantes = os.path.join(diretorio_atual, 'comprovantes')
    
    if not os.path.exists(pasta_comprovantes):
        os.makedirs(pasta_comprovantes)

    caminho = os.path.join(pasta_comprovantes, f'comprovante_{id}.txt')

    with open(caminho, 'w', encoding='utf-8') as arquivo:
        arquivo.write("==== Comprovante de Transferência ====\n")
        arquivo.write(f"==== ID da Transação: {id}\n")
        arquivo.write(f"==== Nome: {nome}\n")
        arquivo.write(f"==== CPF: {cpf}\n")
        arquivo.write(f"==== Banco: {banco}\n")
        arquivo.write(f"==== Agência: {agencia}\n")
        arquivo.write(f"==== Conta: {conta}\n")
        arquivo.write(f"==== Valor: {valor_servico}\n")
        arquivo.write(f"==== Data: {data}\n")
        arquivo.write("======================================\n")

    print(f"Comprovante emitido: {caminho}")

#Função para validação do cpf
def validar_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    return True

#Função para validação da agência
def validar_agencia(agencia):
    if len(agencia) != 4 or not agencia.isdigit():
        return False
    return True

#Função para validar a conta
def validar_conta(conta):
    if len(conta) != 6 or not conta.isdigit():
        return False
    return True

#Função para validação da data
def validar_data(data):
    try:
        data_obj = datetime.strptime(data, '%d/%m/%Y')
        return data_obj >= datetime.now()
    except ValueError:
        return False

#Função principal para o usuário preencher o formulario
def main(valor):
    criar_tabela()
    print("\n== Formulário de Transferência ==")
    nome = passar_nome_user("exemplo")

    cpf = input("CPF: ")
    while not validar_cpf(cpf):
        print("CPF inválido. Use o formato padrão somente com números.")
        cpf = input("CPF: ")

    banco = input("Banco: ")
    agencia = input("Agência: ")
    while not validar_agencia(agencia):
        print("Agência inválida, deve conter apenas números.")
        agencia = input("Agência: ")

    conta = input("Conta: ")
    while not validar_conta(conta):
        print("Conta inválida, deve conter apenas números sem o dígito.")
        conta = input("Conta: ")

    valor_servico = valor

    data = input("Data da Transferência (DD/MM/YYYY): ")
    while not validar_data(data):
        print("Data de transferência inválida. Use o formato DD/MM/YYYY.")
        data = input("Data da transferência (DD/MM/YYYY): ")

    if not verificacao(nome, conta):
        id = inserir_dados(nome, cpf, banco, agencia, conta, valor_servico, data)
        encerrar()
        print("Dados da transferência salvos com sucesso.")
        print("\nSua consulta foi marcada com sucesso!")
        emissao_comprovante(id, nome, cpf, banco, agencia, conta, valor_servico, data)
    else:
        print("Este registro já existe no banco de dados.")

if __name__ == "__main__":
    main(0)