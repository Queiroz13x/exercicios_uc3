'''
Ler indeterminados nomes e imprimir nome de nomes lidos

'''        


r = ''
quantidade = 0
while True:
    nome = input('Informe nome: ')
    quantidade +=1 
    r=input('Deseja continuar? (S/N) ')
    if r.lower()== 'n':
        break
print(f'A quantidade de nomes: {quantidade}')