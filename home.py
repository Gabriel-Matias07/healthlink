# Funções já fornecidas
def passar_nome_user(nome):
    return nome

def passar_nome_prof(nome):
    return nome

def passar_preferencias_contratacao_user(preferencias):
    return preferencias

def passar_informacoes_profissional(info):
    return info

# Funções adicionais
def mostrar_informacoes_profissionais(profissionais):
    print("\n--- Profissionais Disponíveis ---")
    for idx, prof in enumerate(profissionais):
        print(f"{idx + 1}. Nome: {prof['nome']}")
        print(f"   Especialidade: {prof['especialidade']}")
        print(f"   Avaliação: {prof['avaliacao']}/5")
        print(f"   Localização: {prof['localizacao']}")
        print(f"   Horário de atendimento: {prof['horario']}")
        print(f"   Contato: {prof['contato']}")
        print()

def escolher_profissional(profissionais):
    while True:
        try:
            escolha = int(input("Selecione o número do profissional (ou 0 para voltar): "))
            if escolha == 0:
                return None
            elif 1 <= escolha <= len(profissionais):
                return profissionais[escolha - 1]
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

def tela_pagamento(profissional):
    print(f"\nVocê escolheu o profissional {profissional['nome']}.")
    print("Redirecionando para a tela de pagamento...\n")
    # Aqui a chamada para a função que já existe para a tela de pagamento seria implementada
    # Exemplo:
    # chamar_tela_pagamento(profissional)
    print("Tela de pagamento concluída (exemplo).\n")

def voltar_login():
    print("\nVoltando para a tela de login...\n")
    # Aqui você chamaria a função de login já existente
    # Exemplo:
    # chamar_tela_login()

def encerrar_programa():
    print("\nEncerrando o programa. Até logo!\n")
    exit()

def menu_principal(profissionais):
    while True:
        print("\n--- Menu Principal ---")
        print("1. Ver informações dos profissionais")
        print("2. Escolher um profissional")
        print("3. Ir para tela de pagamento")
        print("4. Voltar para o login")
        print("5. Encerrar o programa")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            mostrar_informacoes_profissionais(profissionais)
        elif escolha == "2":
            profissional_escolhido = escolher_profissional(profissionais)
            if profissional_escolhido:
                print(f"\nVocê escolheu o profissional: {profissional_escolhido['nome']}")
        elif escolha == "3":
            if 'profissional_escolhido' in locals() and profissional_escolhido:
                tela_pagamento(profissional_escolhido)
            else:
                print("\nVocê precisa escolher um profissional antes de ir para a tela de pagamento.")
        elif escolha == "4":
            voltar_login()
            break
        elif escolha == "5":
            encerrar_programa()
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Exemplo de dados de profissionais (você pode substituir por dados reais)
profissionais = [
    {
        'nome': 'Dr. João Silva',
        'especialidade': 'Cardiologista',
        'avaliacao': 4.8,
        'localizacao': 'Rua A, 123 - São Paulo, SP',
        'horario': '09:00 - 18:00',
        'contato': '(11) 98765-4321'
    },
    {
        'nome': 'Dra. Maria Souza',
        'especialidade': 'Dermatologista',
        'avaliacao': 4.5,
        'localizacao': 'Rua B, 456 - Rio de Janeiro, RJ',
        'horario': '10:00 - 17:00',
        'contato': '(21) 91234-5678'
    },
    {
        'nome': 'Dr. Pedro Almeida',
        'especialidade': 'Ortopedista',
        'avaliacao': 4.7,
        'localizacao': 'Rua C, 789 - Belo Horizonte, MG',
        'horario': '08:00 - 16:00',
        'contato': '(31) 99876-5432'
    }
]

# Iniciar o programa
if __name__ == "__main__":
    print("Bem-vindo ao Sistema de Contratação de Profissionais!")
    menu_principal(profissionais)
