import sys
from config_precos import adicionar_preco, atualizar_preco, exibir_precos

def menu_profissional():
        print("\n== Menu do Profissional ==")
        print("1. Adicionar Preço")
        print("2. Atualizar Preço")
        print("3. Exibir Preços")
        print("4. Sair")
        
        escolha = input("\nEscolha uma opção: ")
        
        match escolha:
            case '1':
                tipo_servico = input("Tipo de Serviço: ")
                preco = float(input("Preço: "))
                adicionar_preco(tipo_servico, preco)
                print("Preço adicionado com sucesso.")
            case '2':
                id = int(input("ID do Preço a ser atualizado: "))
                preco = float(input("Novo Preço: "))
                atualizar_preco(id, preco)
                print("Preço atualizado com sucesso.")
            case '3':
                exibir_precos()
            case '4':
                print("Saindo...")
                sys.exit()
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_profissional()