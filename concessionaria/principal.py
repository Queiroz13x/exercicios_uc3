''' 07/06/2024
Uma concessionária necessita de um programa que fará o cadastro de 
automóveis que serão comercializados pela mesma.
Cada veículo possui os seguintes campos: Nome, ano, valor, descrição, e se Okm ou usado.
Faça a leitura dos automóveis até o usuário decidir não continuar com a leitura.
Ao terminar a leitura, o programa deverá listar todos os veículos cadastrados.
'''

from funcoes import cadastrar, listarMarca, listarVeiculos, marca 
frota =  []
while True:
    print('Concessionária')
    print('1 - Cadastrar veículos ')
    print('2 - Listar veículos')
    print('3 - Cadastrar marcas')
    print('4 - Listar marcas')
    print('5 - Cadastrar cliente')
    print('0 - Sair')
   
    try:
        opcao = int(input('Digite opção: '))
        match(opcao):
            case 1:
                cadastrar(frota)
            case 2:
                listarVeiculos(frota)
            case 3:
                marca(frota)
            case 4:
                listarMarca(frota)
            case 5:
                cadastrarCliente(frota)


            case 0:
                print('Até a próxima!')
                break
            case _:
                print('Opção inválida')
    except:
        print('Erro na seleção da opção')
