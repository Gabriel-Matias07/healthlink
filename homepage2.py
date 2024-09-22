import utils  
import database 
import sys

RESET = "\033[0;0m" 
RED  = "\033[1;31m"

def listar_profissionais():
    profissionais = database.listar_profissionais_db()
    print("\nLista de Profissionais:")
    for i, profissional in enumerate(profissionais, 1):
        print(f"{i}. {profissional[1]} - {profissional[2]} ({profissional[3]} estrelas)")
    return profissionais  

def perfil(profissionais):
    escolha = input("\nDigite o número do profissional para ver mais detalhes ou pressione Enter para voltar: ")
    if escolha.isdigit():
        escolha = int(escolha)
        if 1 <= escolha <= len(profissionais):
            profissional_id = profissionais[escolha - 1][0]  # Assume que o ID está na primeira posição
            detalhes = database.obter_perfil_db(profissional_id)
            if detalhes:
                print(f"\nDetalhes do Profissional: {detalhes[0]}")
                print(f"Especialidade: {detalhes[1]}")
                print(f"Avaliação: {detalhes[2]} estrelas")
                print(f"Localização: {detalhes[3]}")
                print(f"Horário de Atendimento: {detalhes[4]}")
                print(f"Contato: {detalhes[5]}")
            else:
                print("Detalhes do profissional não encontrados.")
        else:
            print("Número inválido.")
    else:
        print("Retornando ao menu principal.")

def filtrar_profissionais():
    especialidade = input("\nDigite a especialidade para buscar (ou pressione Enter para todas): ").lower()
    localizacao = input("Digite a localização para buscar (ou pressione Enter para todas): ").lower()

    profissionais = database.filtrar_profissionais_db(especialidade, localizacao)

    print("\nResultados da busca:")
    if profissionais:
        for i, profissional in enumerate(profissionais, 1):
            print(f"{i}. {profissional[1]} - {profissional[2]} ({profissional[3]} estrelas)")
    else:
        print("Nenhum profissional encontrado.")

def menu_principal():
    while True:
        print("""
--------------------------------------------------------------
""" + RED + """
======================= HealthLink✝️  =======================
""" + RESET + """--------------------------------------------------------------
""" + RED + """Para ajudarmos da melhor forma precisamos saber qual operação deseja realizar:""" + RESET + """
| [""" + RED + """1""" + RESET + """] Listar Profissionais                   |
| [""" + RED + """2""" + RESET + """] Filtrar Profissionais                  |
| [""" + RED + """3""" + RESET + """] Sair                                   |
--------------------------------------------------------------""")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            profissionais = listar_profissionais()
            perfil(profissionais)
        elif opcao == '2':
            filtrar_profissionais()
        elif opcao == '3':
            print("Saindo do sistema...")
            utils.encerrar()
            return
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    utils.carregamento()
    menu_principal()
