RESET = "\033[0;0m"
RED  = "\033[1;31m"

profissionais = [
    {
        "nome": "Dr. João Silva",
        "especialidade": "Cardiologista",
        "avaliacao": 4.5,
        "localizacao": "Centro",
        "horario": "08:00 - 17:00",
        "contato": "joao.silva@healthlink.com"
    },
    {
        "nome": "Dra. Maria Santos",
        "especialidade": "Dermatologista",
        "avaliacao": 4.8,
        "localizacao": "Zona Sul",
        "horario": "09:00 - 18:00",
        "contato": "maria.santos@healthlink.com"
    },
    {
        "nome": "Dr. Carlos Oliveira",
        "especialidade": "Pediatra",
        "avaliacao": 4.2,
        "localizacao": "Zona Oeste",
        "horario": "08:00 - 16:00",
        "contato": "carlos.oliveira@healthlink.com"
    },
    {
        "nome": "Dra. Evelyne Arrais",
        "especialidade": "Esteticista",
        "avaliacao": 4.8,
        "localizacao": "Zona Norte",
        "horario": "08:00 - 18:00",
        "contato": "evelyne.arrais@healthlink.com"
    },
    {
        "nome": "Caio Nogueira",
        "especialidade": "Enfermeiro",
        "avaliacao": 4.0,
        "localizacao": "centro",
        "horario": "22:00 - 06:00",
        "contato": "caio.nogueira@healthlink.com"
    }
]

def listar_profissionais():
    print("\nLista de Profissionais:")
    for i, profissional in enumerate(profissionais, 1):
        print(f"{i}. {profissional['nome']} - {profissional['especialidade']} ({profissional['avaliacao']} estrelas)")

def perfil(index):
    profissional = profissionais[index]
    print(f"\nDetalhes do Profissional: {profissional['nome']}")
    print(f"Especialidade: {profissional['especialidade']}")
    print(f"Avaliação: {profissional['avaliacao']} estrelas")
    print(f"Localização: {profissional['localizacao']}")
    print(f"Horário de Atendimento: {profissional['horario']}")
    print(f"Contato: {profissional['contato']}")

def filtrar_profissionais():
    especialidade = input("\nDigite a especialidade para buscar (ou pressione Enter para todas): ").lower()
    localizacao = input("Digite a localização para buscar (ou pressione Enter para todas): ").lower()

    print("\nResultados da busca:")
    for i, profissional in enumerate(profissionais, 1):
        if (not especialidade or especialidade in profissional['especialidade'].lower()) and \
           (not localizacao or localizacao in profissional['localizacao'].lower()):
            print(f"{i}. {profissional['nome']} - {profissional['especialidade']} ({profissional['avaliacao']} estrelas)")

def menu_principal():
    while True:
        print(""""""
"""--------------------------------------------------------------"""
+ RED + """
======================= HealthLink✝️  ======================="""
+RESET+"""
--------------------------------------------------------------
"""+RED+"""Para ajudarmos da melhor forma precisamos saber qual operação deseja realizar:"""+RESET+"""
| ["""+RED+"""1"""+RESET+"""] Listar Profissionais                   |
| ["""+RED+"""2"""+RESET+"""] Filtrar Profissionais                    |
| ["""+RED+"""3"""+RESET+"""] Sair                                       |
--------------------------------------------------------------""") 
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            listar_profissionais()
            escolha = input("\nDigite o número do profissional para ver mais detalhes ou pressione Enter para voltar: ")
            if escolha.isdigit() and 1 <= int(escolha) <= len(profissionais):
                perfil(int(escolha) - 1)
        elif opcao == '2':
            filtrar_profissionais()
        elif opcao == '3':
            print("Saindo do sistema...")
            return
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()

