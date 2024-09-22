#Módulo para redirecionar as escolhas de usuário ou profissional

import login_user, login_profissionais
#Função que recebe qual valor e redireciona corretamente
def redirecionar(retorno):
    dado_retornado = retorno
    usuario = "usuário"
    profissional = "profissional"   
    if dado_retornado == usuario:
        return login_user.form_usuario(dado_retornado)
    elif dado_retornado == profissional:
        return login_profissionais.form_profissional(dado_retornado)
    else:
        print(f"Retorno inesperado: {dado_retornado}")