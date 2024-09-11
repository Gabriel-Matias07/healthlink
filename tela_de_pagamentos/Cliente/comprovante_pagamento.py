import os

#Função para criação do comprovante de pagamento
def emissao_comprovante(id, nome, cpf, banco, agencia, conta, valor, data):
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))
    caminho = os.path.join(diretorio_atual, f'comprovante_{id}.txt')

    with open(caminho, 'w', encoding='utf-8') as arquivo:
        arquivo.write("==== Comprovante de Transferência ====\n")
        arquivo.write(f"==== ID da Transação: {id}\n")
        arquivo.write(f"==== Nome: {nome}\n")
        arquivo.write(f"==== CPF: {cpf}\n")
        arquivo.write(f"==== Banco: {banco}\n")
        arquivo.write(f"==== Agência: {agencia}\n")
        arquivo.write(f"==== Conta: {conta}\n")
        arquivo.write(f"==== Valor: {valor}\n")
        arquivo.write(f"==== Data: {data}\n")
        arquivo.write("======================================\n")

    print(f"Comprovante emitido: {caminho}")