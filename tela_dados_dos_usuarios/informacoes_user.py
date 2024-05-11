import sqlite3
import time

def pegar_informacoes():

    t = 3 #Da bliblioteca time

    print("--Digite seu telefone--")
    telefone = int(input())
    print("--Digite seu endereço--")
    endereco = str(input())
    print("--Digite sua data de nascimento separado por '-'. Exemplo: '17-09-2003'")
    data_nascimento = str(input())
    print("--Digite seu gênero--")
    genero = str(input())

    print("Informações: \n")
    print(f"Telefone: {telefone}\n Endereço: {endereco}\n Data de Nascimento: {data_nascimento}\n Gênero: {genero}\n")
    print("Deseja alterar alguma informação? S = Sim, N = Não")
    alteracao = str(input())

    #Condição de alteração
    
    if 'S' in alteracao:
        print("\n")
        print("1 - Telefone\n 2 - Endereço\n 3 - Data de Nascimento\n 4 - Gênero\n")
        selecao_campo = str(input())
        if selecao_campo == '1':
            telefone = int(input("Digite o seu telefone: "))
        elif selecao_campo == '2':
            endereco = str(input("Digite o seu endereço: "))
        elif selecao_campo == '3':
            data_nascimento = str(input("Digite sua data de nascimento: "))
        elif genero == '4':
            str(input("Digite seu gênero: "))
    elif 'N' in alteracao:
        #Jogar informações no banco de dados
        print("Realizando conexão...")
        time.sleep(t)
        print("Inserindo no banco de dados...")
        time.sleep(t)
        armazenar(telefone, endereco, data_nascimento, genero)
        print("Cadastro realizado com sucesso!")
        exit()
    else:
        return 'Inválido', None
    
    print("Alteração feita com sucesso!\n")
    print("Informações: \n")
    print(f"Telefone: {telefone}\n Endereço: {endereco}\n Data de Nascimento: {data_nascimento}\n Gênero: {genero}\n")
    print("Realizando conexão...")
    time.sleep(t)
    print("Inserindo no banco de dados...")
    time.sleep(t)

    #Jogar informações no banco de dados
    armazenar(telefone, endereco, data_nascimento, genero)
    print("Cadastro realizado com sucesso!")

#Função para armazenar dados no banco de dados

def armazenar(telefone, endereco, nascimento, genero):
    erro = False
    try:
        banco = sqlite3.connect("data_user_cadastro.db")
        cursor = banco.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS data_user_cadastro(telefone, endereco, nascimento, genero)")
        cursor.execute("INSERT INTO data_user_cadastro VALUES (?, ?, ?, ?)", (telefone, endereco, nascimento, genero))
        banco.commit()
        banco.close()
    except sqlite3.Error as error:
        print(error)
        erro = True
    return erro

#Chamando a função  (Será chamada no main.py)
pegar_informacoes()