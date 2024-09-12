from Cliente import formulario_cartao, formulario_boleto, formulario_transferencia
from Geral import config_precos
import sys

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
                print("Escolha o seu agendamento: ")
                menu_formularios()
        case '2':
            sys.exit()

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