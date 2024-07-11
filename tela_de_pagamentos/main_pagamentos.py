import sqlite3, os
from usuario import menu_principal_usuario

def criar_tabela():
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'dados_bancarios_user.db')
    
    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS dados_bancarios_user (
                        id INTEGER PRIMARY KEY,
                        nome TEXT,
                        num_conta TEXT,
                        saldo REAL)''')
    conexao.commit()
    conexao.close()

def inserir_dados(nome, num_conta, saldo):
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'dados_bancarios_user.db')
    
    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO dados_bancarios_user (nome, num_conta, saldo)
                      VALUES (?, ?, ?)''', (nome, num_conta, saldo))
    conexao.commit()
    conexao.close()
    
def verificacao(nome, num_conta):
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'dados_bancarios_user.db')
    
    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM dados_bancarios_user WHERE nome = ? AND num_conta = ?''', (nome, num_conta))
    resultado = cursor.fetchone()
    conexao.close()
    return resultado is not None

def verificacao_saldo(saldo):
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'dados_bancarios_user.db')
    
    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM dados_bancarios_user WHERE saldo = ?''', (saldo))
    resultado = cursor.fetchone()
    conexao.close()
    return resultado is not None

def main():
    criar_tabela()
    nome, num_conta, saldo = menu_principal_usuario()

    if not verificacao(nome, num_conta):
        inserir_dados(nome, num_conta, saldo)
        print("Dados Salvos.")
    else:
        print("Este registro já existe no banco de dados.")
        
    

if __name__ == "__main__":
    main()