import sqlite3
import os

def tabela_cartao():
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'cartoes.db')

    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()

    cursor.execute('''create table if not exists cartao (
                    id INTEGER PRIMARY KEY,
                    nome TEXT,
                    numero TEXT,
                    data_validade TEXT,
                    cvv TEXT)''')

    conexao.commit()
    conexao.close()
    
    
def verificar_cartao_existente(numero):
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'cartoes.db')

    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM cartao WHERE numero=?", (numero,))
    cartao = cursor.fetchone()
    
    conexao.close()
    return cartao is not None

def inserir_cartao(nome, numero, data_validade, cvv):
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'cartoes.db')

    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()

    cursor.execute('''insert into cartao (nome, numero, data_validade, cvv)
                    values (?, ?, ?, ?)''', (nome, numero, data_validade, cvv))

    conexao.commit()
    conexao.close()
    
def main():
    tabela_cartao()
    print("== Formulário do Cartão ==")
    nome = input("Nome do titular do cartão: ")
    if not nome:
        print("Erro: preencha corretamente o campo.")
    else:
        numero = input("Número do Cartão: ")
        if len(numero) != 19 or not numero:
            print("Erro: O número do cartão deve conter 19 caracteres com os espaços.")
        else:
            data_validade = input("Data de Validade (MM/AA): ")
            if len(data_validade) != 5 or not data_validade[:2].isdigit() or not data_validade[2] == '/' or not data_validade[3:].isdigit() or not data_validade:
                print("Erro: Data de validade inválida, utilize o formato MM/AA.")
            else:
                cvv = input("CVV: ")
                if len(cvv) != 3 or not cvv.isdigit() or not cvv:
                    print("Erro: CVV inválido, pois deve conter exatamente 3 dígitos.")
                else:
                    if verificar_cartao_existente(numero):
                        print("\nErro, cartão já cadastrado!")
                    else:
                        inserir_cartao(nome, numero, data_validade, cvv)
                        print("\nCartão salvo com sucesso!")
    
if __name__ == "__main__":
    main()