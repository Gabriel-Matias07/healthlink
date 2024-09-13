import sqlite3, os

# Função para criar a tabela de agendamentos
def criar_tabela_agendamentos():
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'agendamentos.db')
    
    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS agendamento (
                        id INTEGER PRIMARY KEY,
                        servico TEXT,
                        valor TEXT,
                        data_agendamento TEXT)''')
    conexao.commit()
    conexao.close()

# Função para inserir dados no banco de agendamentos
def inserir_dados_agendamento(servico, valor, data_agendamento):
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'agendamentos.db')
    
    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO agendamento (servico, valor, data_agendamento)
                      VALUES (?, ?, ?)''', (servico, valor, data_agendamento))
    conexao.commit()
    id = cursor.lastrowid
    conexao.close()
    return id

if __name__ == "__main__":
    criar_tabela_agendamentos()