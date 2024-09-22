import sys
from config_precos3 import adicionar_preco, atualizar_preco, exibir_precos, adicionar_datas_disponiveis, remover_data_disponivel, tabela_precos
from utils1 import encerrar, clear

#Função principal do profissional, onde ele vai escolher o que fazer com seus serviços e valores
def menu_profissional():
    while True:
        print("\n== Menu do Profissional ==")
        print("1. Adicionar Preço")
        print("2. Atualizar Preço")
        print("3. Adicionar Datas Disponíveis")
        print("4. Remover Data Disponível")
        print("5. Exibir Preços")
        print("6. Sair")
        
        escolha = input("\nEscolha uma opção: ")

        match escolha:
            case '1':
                tipo_servico = input("Tipo de Serviço: ")
                preco = float(input("Preço: "))
                datas_disponiveis = []
                continuar = True
                while continuar:
                    data = input("Digite uma data disponível (ou '0' para terminar): ")
                    if data == '0':
                        continuar = False
                    elif data:
                        datas_disponiveis.append(data)
                if datas_disponiveis:
                    adicionar_preco(tipo_servico, preco, datas_disponiveis)
                    print("Preço adicionado com sucesso.")
                else:
                    print("Nenhuma data foi adicionada.")
                clear()

            case '2':
                id = int(input("ID do Preço a ser atualizado: "))
                preco = float(input("Novo Preço: "))
                atualizar_preco(id, preco)
                print("Preço atualizado com sucesso.")
                clear()
            case '3':
                id = int(input("ID do Preço para adicionar datas: "))
                novas_datas = []
                seguir = True
                while seguir:
                    data = input("Digite uma nova data disponível (ou '0' para terminar): ")
                    if data == '0':
                        seguir = False
                    elif data:
                        novas_datas.append(data)
                if novas_datas:
                    adicionar_datas_disponiveis(id, novas_datas)
                    print("Datas adicionadas com sucesso.")
                else:
                    print("Nenhuma data foi adicionada.")
                clear()
            case '4':
                id = int(input("ID do Preço para remover data: "))
                data = input("Data a ser removida: ")
                remover_data_disponivel(id, data)
                print("Data removida com sucesso.")
                clear()
            case '5':
                exibir_precos()
            case '6':
                encerrar()
                sys.exit()

            case _:
                print("Opção inválida. Tente novamente.")
                clear()

if __name__ == "__main__":
    tabela_precos()
    menu_profissional()