'''
Escreve um algoritimo que leia um número, o
programa calculará e exibirá a tabua deste número.
Mostre a tabuada na forma:

'''

numero = int(input('Informe um numero: '))
for i in  range (1,11):
    r = numero * i 
    print(f'{i} x {numero} = {r}')
