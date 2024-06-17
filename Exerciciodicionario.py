''' 07/06/2024
Uma concessionária necessita de um programa que fará o cadastro de 
automóveis que serão comercializados pela mesma.
Cada veículo possui os seguintes campos: Nome, ano, valor, descrição, e se Okm ou usado.
Faça a leitura dos automóveis até o usuário decidir não continuar com a leitura.
Ao terminar a leitura, o programa deverá listar todos os veículos cadastrados.
'''
agenda = []

while True:
    veiculo = {}
    veiculo['NOME'] =     input('Infome o nome do veiculo:')
    veiculo['ANO'] = int(input('Informe o ano:')) 
    veiculo['VALOR'] =     input('Informe o valor: R$')
    veiculo['DESCRIÇÃO'] =     input('Informe a descrição:')
    veiculo['KM'] =     input('OKM OU USADO:')

    agenda.append(veiculo)
    r = input('Deseja continuar (S/N) ?' ).lower()
    if r == 'n':
        break

for contato in agenda:
    print(f"Nome: {contato['NOME']} - Valor: R$ {contato['VALOR']} - 'Ano: {contato['ANO']} - 'DESCRIÇÃO: {contato['DESCRIÇÃO']} - 'KM {contato['KM']} ")
