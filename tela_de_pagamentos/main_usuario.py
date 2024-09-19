from cliente import formulario_cartao, formulario_boleto, formulario_transferencia
from profissional import config_precos, agendamentos
import sys, os, sqlite3
from login_cadastro.main1 import escolher_opcao

def menu_principal():
    while True:
        print("Bem-vindo à tela de pagamentos, caro usuário.")
        print("== Menu Principal ==")
        print("1. Mostrar Preços e serviços")
        print("2. Sair")
        escolha = input("Escolha uma opção: ")

        match escolha:
            case '1':
                precos = config_precos.exibir_precos()
                
                if not precos:
                    print("Não há serviços disponíveis no momento.")
                    continue

                if not verificar_datas_disponiveis(precos):
                    print("Todos os serviços disponíveis não possuem datas disponíveis.")
                    continue

                opcao_agenda = input("\nGostaria de fazer um agendamento? (digite 1 para continuar ou 0 para sair): ")
                if opcao_agenda == '1':
                    escolher_agendamento(precos)    
            case '2':
                print("Saindo...")
                sys.exit()
            case _:
                print("Opção inválida. Tente novamente.")

def verificar_datas_disponiveis(precos):
    for servico in precos.values():
        if servico["datas"]:
            return True
    
    return False

def obter_valor_servico(tipo_servico):
    caminho_bd = os.path.join(os.path.dirname(__file__), 'Profissional', 'precos.db')
    
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
    
def escolher_agendamento(precos):
    nome = input("\nDigite o seu nome completo: ")
    
    servicos = list(precos.keys())
    if not servicos:
        print("Nenhum serviço disponível no momento.")
        return

    print("\nServiços disponíveis:")
    for i, servico in enumerate(servicos, start=1):
        print(f"{i}. {servico}")

    escolha_servico = input("Escolha o número do serviço desejado: ")
    
    try:
        escolha_index = int(escolha_servico) - 1
        if 0 <= escolha_index < len(servicos):
            servico = servicos[escolha_index]
        else:
            print("Escolha inválida. Tente novamente.")
            return
    except ValueError:
        print("Entrada inválida. Tente novamente.")
        return

    datas_disponiveis = precos[servico]["datas"]
    if not datas_disponiveis:
        print(f"\nO serviço '{servico}' não possui datas disponíveis no momento.")
        return

    print(f"\nDatas disponíveis para o serviço '{servico}':")
    for i, data in enumerate(datas_disponiveis, start=1):
        print(f"{i}. {data}")

    escolha_data = input("Escolha o número da data desejada: ")
    
    try:
        escolha_index = int(escolha_data) - 1
        if 0 <= escolha_index < len(datas_disponiveis):
            data_agendamento = datas_disponiveis[escolha_index]
        else:
            print("Escolha inválida. Tente novamente.")
            return
    except ValueError:
        print("Entrada inválida. Tente novamente.")
        return

    valor = obter_valor_servico(servico)
    
    if valor is None:
        print(f"\nServiço '{servico}' não encontrado. Tente novamente.")
        return

    try:
        valor_num = float(valor)
        print(f"\nO valor do serviço '{servico}' é R${valor_num:.2f}.")
    except ValueError:
        print(f"\nValor retornado para o serviço '{servico}' é inválido: {valor}")
        return

    confirmar = input("Deseja confirmar o agendamento com este valor? (digite 1 para confirmar ou 0 para encerrar): ")
    if confirmar == '1':
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
    print("4 - Voltar para o menu")
    
    opcao = input("Opção: ")
    
    match opcao:
        case '1':
            formulario_cartao.main()
        case '2':
            formulario_boleto.main()
        case '3':
            formulario_transferencia.main()
        case '4':
            return
        case _:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":  
    menu_principal()