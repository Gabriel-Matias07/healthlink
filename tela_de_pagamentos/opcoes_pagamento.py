import formulario_cartao

def opcoes_pagamento():
    print("Escolha uma opção de pagamento:")
    print("1 - Cartão de crédito")
    print("2 - Boleto")
    print("3 - Transferência")
    
    opcao = input("Opção: ")
    
    match opcao:
        case '1':
            formulario_cartao.main()
        case '2':
            print("Pagamento por cartão de débito.")
        case '3':
            print("Pagamento via PIX.")
        case _:
            print("Opção inválida.")

opcoes_pagamento()