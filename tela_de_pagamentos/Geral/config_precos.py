import sqlite3, os

def tabela_precos():
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'plataforma.db')
    
    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS precos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        profissional_id INTEGER,
                        tipo_servico TEXT,
                        preco REAL,
                        FOREIGN KEY (profissional_id) REFERENCES profissionais(id)
                    )''')
    
    conexao.commit()
    conexao.close()

def adicionar_preco(profissional_id, tipo_servico, preco):
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'plataforma.db')
    
    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()
    
    cursor.execute('''INSERT INTO precos (profissional_id, tipo_servico, preco)
                      VALUES (?, ?, ?)''', (profissional_id, tipo_servico, preco))
    
    conexao.commit()
    conexao.close()

def atualizar_preco(id, preco):
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'plataforma.db')
    
    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()
    
    cursor.execute('''UPDATE precos SET preco = ? WHERE id = ?''', (preco, id))
    
    conexao.commit()
    conexao.close()

def exibir_precos(profissional_id):
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'plataforma.db')
    
    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()
    
    cursor.execute('''SELECT tipo_servico, preco FROM precos WHERE profissional_id = ?''', (profissional_id,))
    precos = cursor.fetchall()
    
    conexao.close()
    
    print("== Preços do Profissional ==")
    for tipo_servico, preco in precos:
        print(f"{tipo_servico}: R${preco:.2f}")

if __name__ == "__main__":
    tabela_precos()