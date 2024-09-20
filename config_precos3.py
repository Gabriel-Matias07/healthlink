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
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS datas_disponiveis (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        preco_id INTEGER,
                        data TEXT,
                        FOREIGN KEY(preco_id) REFERENCES precos(id)
                    )''')
    
    conexao.commit()
    conexao.close()

def obter_valor_servico(tipo_servico):
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'precos.db')

    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()

    cursor.execute('''SELECT preco FROM precos WHERE tipo_servico = ?''', (tipo_servico,))
    resultado = cursor.fetchone()

    conexao.close()
    print(f"Buscando valor para o serviço: {tipo_servico}")
    if resultado:
        return resultado[0]
    return None
    

def adicionar_preco(tipo_servico, preco, datas_disponiveis):
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'precos.db')
    
    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()
    
    cursor.execute('''INSERT INTO precos (tipo_servico, preco)
                      VALUES (?, ?)''', (tipo_servico, preco))
    preco_id = cursor.lastrowid
    
    for data in datas_disponiveis:
        cursor.execute('''INSERT INTO datas_disponiveis (preco_id, data)
                          VALUES (?, ?)''', (preco_id, data))
    
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

def adicionar_datas_disponiveis(preco_id, novas_datas):
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'precos.db')
    
    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()
    
    for data in novas_datas:
        cursor.execute('''INSERT INTO datas_disponiveis (preco_id, data)
                          VALUES (?, ?)''', (preco_id, data))
    
    conexao.commit()
    conexao.close()

def remover_data_disponivel(preco_id, data):
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'precos.db')
    
    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()
    
    cursor.execute('''DELETE FROM datas_disponiveis WHERE preco_id = ? AND data = ?''', (preco_id, data))
    
    conexao.commit()
    conexao.close()

def exibir_precos():
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'precos.db')
    
    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()

    cursor.execute('''SELECT p.id, p.tipo_servico, p.preco, d.data
                      FROM precos p
                      LEFT JOIN datas_disponiveis d ON p.id = d.preco_id''')
    resultados = cursor.fetchall()
    
    conexao.close()
    
    precos = {}
    for id, tipo_servico, preco, data in resultados:
        if tipo_servico not in precos:
            precos[tipo_servico] = {"preco": preco, "datas": []}
        if data:
            precos[tipo_servico]["datas"].append(data)

    print("\n== Preços dos Serviços ==")
    for tipo_servico, info in precos.items():
        try:
            preco = float(info["preco"])
            datas = ", ".join(info["datas"]) if info["datas"] else "Nenhuma data disponível"
            print(f"{tipo_servico}: R${preco:.2f}")
            print(f"  Datas Disponíveis: {datas}")
        except ValueError:
            print(f"Erro ao formatar o preço para o serviço: {tipo_servico}")
    
    return precos