import sqlite3, os

def tabela_precos():
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'precos.db')
    
    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS precos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        tipo_servico TEXT,
                        preco TEXT
                    )''')
    
    conexao.commit()
    conexao.close()

def adicionar_preco(tipo_servico, preco):
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'precos.db')
    
    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()
    
    cursor.execute('''INSERT INTO precos (tipo_servico, preco)
                      VALUES (?, ?)''', (tipo_servico, preco))
    
    conexao.commit()
    conexao.close()

def atualizar_preco(id, preco):
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'precos.db')
    
    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()
    
    cursor.execute('''UPDATE precos SET preco = ? WHERE id = ?''', (preco, id))
    
    conexao.commit()
    conexao.close()

def exibir_precos():
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'precos.db')
    
    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()

    cursor.execute('''SELECT tipo_servico, preco FROM precos''')
    precos = cursor.fetchall()
    
    conexao.close()
    
    print("== Preços dos Serviços ==")
    for tipo_servico, preco in precos:
        try:
            preco = float(preco)
            print(f"{tipo_servico}: R${preco:.2f}")
        except ValueError:
            print(f"Erro ao formatar o preço para o serviço: {tipo_servico}")

if __name__ == "__main__":
    tabela_precos()