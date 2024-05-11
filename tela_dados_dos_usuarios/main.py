import informacoes_user
from profissionais import informacoes_prof

def main():
    print("---Bem vindo(a) a tela de cadastro de informações gerais---")
    print("---Aqui você pode personalizar os seus gostos antes de acessar nosso sistema---")

    #Chama a função que retorna user ou prof
    #example.function()
    #Uma conexão será feita entre a tela de login (main) e a tela de cadastro (essa main), então será retornada alguma informação indicando se o usuário cadastrado é um cliente ou profissional, logo os dados serão adaptados para tal.

    #Estrutura de escolhas
    if(): #if user:
        #Chama a função pegar_informacoes
        informacoes_user.pegar_informacoes
    elif(): #elif prof:
        #Chama a função alterar_informacoes
        informacoes_prof.alterar_informacoes()
    else:
        #Retorna o fim
        print("-----")

        #Uma função de alterar dados (após inseridos no banco) será adicionada em breve