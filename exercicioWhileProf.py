'''
A prefeitura de uma cidade fez uma pesquisa entre seus habitantes,
coletando dados sobre o salário e número de filhos. A prefeitura deseja saber:

A) Média do salário da população;
B) Média dpo número de filhos;

A condição de parada é perguntar ao usuario se deseja continuar.

'''


resp= ''
totalSalario = 0 
totalFilhos = 0 
quantidade = 0
while True:
    salario = float(input('Informe salário:  '))
    filhos = int(input('informe número de filhos: '))

    totalSalario = totalSalario + salario
    totalFilhos = totalFilhos + filhos
    quantidade += 1 

    resp = input('Deseja continuar? (S/N)').lower()
    if resp == 'n':
        break

mediaSalario = totalSalario / quantidade
mediaFilhos = totalFilhos / quantidade
print(f'A média de salários é {mediaSalario:.2f}')
print(f'A média de filhos é {mediaFilhos:.2f}')
print('FIM')