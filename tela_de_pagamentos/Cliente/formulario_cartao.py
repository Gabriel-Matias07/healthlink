import sqlite3, os, datetime
import Profissional.agendamentos
# Função para criar o banco de dados dos cartões
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
    

# Função para verificar existência do cartão no banco
def verificar_cartao_existente(numero):
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'cartoes.db')

    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM cartao WHERE numero=?", (numero,))
    cartao = cursor.fetchone()
    
    conexao.close()
    return cartao is not None

# Função para inserir os dados do cartão no banco de dados
def inserir_cartao(nome, numero, data_validade, cvv):
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_bd = os.path.join(diretorio_atual, 'cartoes.db')

    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()

    cursor.execute('''insert into cartao (nome, numero, data_validade, cvv)
                    values (?, ?, ?, ?)''', (nome, numero, data_validade, cvv))

    conexao.commit()
    conexao.close()

# Função principal para o cadastro
def main():
    tabela_cartao()
    print("== Formulário do Cartão ==")
    nome_valido = False
    while not nome_valido:
        nome = input("Nome do titular do cartão: ")
        if nome:
            nome_valido = True
        else:
            print("Erro: preencha corretamente o campo.")
    
    numero_valido = False
    while not numero_valido:
        numero = input("Número do Cartão: ")
        if len(numero) == 16 and numero.replace(' ', '').isdigit():
            numero_valido = True
        else:
            print("Erro: O número do cartão deve conter apenas números.")
    
    data_validade_valida = False
    while not data_validade_valida:
        data_validade = input("Data de Validade (MM/AA): ")
        if len(data_validade) == 5 and data_validade[:2].isdigit() and data_validade[2] == '/' and data_validade[3:].isdigit():
            data_validade_valida = True
        else:
            print("Erro: Data de validade inválida, utilize o formato MM/AA.")
    
    cvv_valido = False
    while not cvv_valido:
        cvv = input("CVV: ")
        if len(cvv) == 3 and cvv.isdigit():
            cvv_valido = True
        else:
            print("Erro: CVV inválido, pois deve conter exatamente 3 dígitos e apenas números.")

    valor = input("Valor da transação: ")
    servico = input("Serviço Escolhido: ")

    data_transacao = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    
    if verificar_cartao_existente(numero):
        print("\nErro, cartão já cadastrado!")
    else:
        inserir_cartao(nome, numero, data_validade, cvv)
        Profissional.agendamentos.inserir_dados_agendamento(servico, valor, data_transacao)
        print("\nCartão Salvo!")
    
if __name__ == "__main__":
    main()