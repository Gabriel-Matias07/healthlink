from Cliente import formulario_cartao, formulario_boleto, formulario_transferencia
from Profissional import config_precos, agendamentos
import sys, os, sqlite3

def menu_principal():
    print("Bem-vindo à tela de pagamentos, caro usuário.")
    print("Vamos prosseguir com o seu atendimento!")
    print("== Menu Principal ==")
    print("1. Mostrar Preços e serviços")
    print("2. Sair")
    escolha = input("Escolha uma opção: ")

    match escolha:
        case '1':
            config_precos.exibir_precos()
            opcao_agenda = input("Gostaria de fazer um agendamento? (s/n): ")
            if opcao_agenda.lower() == 's':
                escolher_agendamento()    
        case '2':
            print("Saindo...")
            sys.exit()

def obter_valor_servico(tipo_servico):
    caminho_bd = 'C:/Users/rodri/OneDrive/Área de Trabalho/Projeto/healthlink/tela_de_pagamentos/Profissional/precos.db'
    
    conexao = sqlite3.connect(caminho_bd)
    cursor = conexao.cursor()
    
    cursor.execute('''
        SELECT preco FROM precos WHERE tipo_servico = ?
    ''', (tipo_servico,))
    
    resultado = cursor.fetchone()
    conexao.close()
    
    if resultado:
        return resultado[0]
    else:
        return None
    
def escolher_agendamento():
    print("Escolha o seu agendamento: ")
    nome = input("Digite o seu nome completo: ")
    servico = input("Insira o tipo de serviço que deseja agendar: ")
    data_agendamento = input("Insira a data (dd/mm/aaaa): ")
    valor = obter_valor_servico(servico)

    if valor is None:
        print(f"Serviço '{servico}' não encontrado. Tente novamente.")
        return

    try:
        valor_num = float(valor)
        print(f"O valor do serviço '{servico}' é R${valor_num:.2f}.")
    except ValueError:
        print(f"Valor retornado para o serviço '{servico}' é inválido: {valor}")
        return

    confirmar = input("Deseja confirmar o agendamento com este valor? (s/n): ")
    if confirmar.lower() == 's':
        try:
            agendamentos.inserir_dados_agendamento(nome, servico, valor_num, data_agendamento)
            print("Agendamento realizado com sucesso!")
            menu_formularios()
        except Exception as e:
            print(f"Erro ao realizar o agendamento: {e}")
    else:
        print("Agendamento não confirmado.")

def menu_formularios():
    print("Escolha uma opção de pagamento:")
    print("1 - Cartão de crédito")
    print("2 - Boleto")
    print("3 - Transferência")
    
    opcao = input("Opção: ")
    
    match opcao:
        case '1':
            formulario_cartao.main()
        case '2':
            formulario_boleto.main()
        case '3':
            formulario_transferencia.main()
        case _:
            print("Opção inválida.")
            return

menu_principal()