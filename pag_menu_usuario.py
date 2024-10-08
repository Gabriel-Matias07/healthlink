import sys, pag_precos, pag_agendamentos, pag_form_boleto, pag_form_cartao, pag_form_transferencia
from login_utils import encerrar, clear

#Função principal para o usuário, onde ele vai marcar a sua consulta
def menu_principal():
    while True:
        print("== Tela de Pagamentos - Menu Principal ==")
        print("1. Mostrar Preços e serviços")
        print("2. Sair")
        escolha = input("Escolha uma opção: ")

        match escolha:
            case '1':
                precos = pag_precos.exibir_precos()

                if not precos:
                    clear()
                    print("Não há serviços disponíveis no momento.\n")
                    continue

                if not verificar_datas_disponiveis(precos):
                    clear()
                    print("Todos os serviços disponíveis não possuem datas disponíveis.")
                    continue

                opcao_agenda = input("\nGostaria de fazer um agendamento? (digite 1 para continuar ou 0 para sair): ")
                clear()
                if opcao_agenda == '1':
                    escolher_agendamento(precos)
            case '2':
                encerrar()
                sys.exit()
            case _:
                print("Opção inválida. Tente novamente.")

#Função para verificação de datas disponíveis
def verificar_datas_disponiveis(precos):
    for servico in precos.values():
        if servico["datas"]:
            return True
    return False

#Função para marcar a consulta
def escolher_agendamento(precos):

    nome = input("Digite o seu nome novamente: ")

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

    valor = pag_precos.obter_valor_servico(servico)

    if valor is None:
        print(f"\nServiço '{servico}' não encontrado. Tente novamente.")
        return

    try:
        valor_num = float(valor)
        clear()
        print(f"\nO valor do serviço '{servico}' é R${valor_num:.2f}.")
    except ValueError:
        print(f"\nValor retornado para o serviço '{servico}' é inválido: {valor}")
        return

    confirmar = input("Deseja confirmar o agendamento com este valor? (digite 1 para confirmar ou 0 para encerrar): ")
    if confirmar == '1':
        try:
            pag_agendamentos.inserir_dados_agendamento(nome, servico, valor_num, data_agendamento)
            print("\nAgendamento realizado com sucesso!")
            clear()
            menu_formularios(valor_num)
        except Exception as e:
            print(f"Erro ao realizar o agendamento: {e}")
    else:
        print("Agendamento não confirmado.")

#Função para escolher a opção de pagamento
def menu_formularios(valor):
    print("Escolha uma opção de pagamento:")
    print("1 - Cartão de crédito")
    print("2 - Boleto")
    print("3 - Transferência")
    print("4 - Voltar para o menu")
    
    opcao = input("Opção: ")
    
    match opcao:
        case '1':
            pag_form_cartao.main()
        case '2':
            pag_form_boleto.main(valor)
        case '3':
            pag_form_transferencia.main(valor)
        case '4':
            return
        case _:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    pag_agendamentos.criar_tabela_agendamentos()  
    menu_principal()