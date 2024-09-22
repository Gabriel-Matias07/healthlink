import sqlite3, os

# Função para criar a tabela de agendamentos
def criar_tabela_agendamentos():
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'consultas.db')
    
    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS consulta (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        servico TEXT,
                        valor REAL,
                        data_agendamento TEXT)''')
    conexao.commit()
    conexao.close()

# Função para inserir dados no banco de agendamentos
def inserir_dados_agendamento(nome, servico, valor, data_agendamento):
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'consultas.db')
    
    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO consulta (nome, servico, valor, data_agendamento)
                      VALUES (?, ?, ?, ?)''', (nome, servico, valor, data_agendamento))
    conexao.commit()
    id = cursor.lastrowid
    conexao.close()
    return id