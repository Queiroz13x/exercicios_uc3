'''
Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
a) a idade dessa pessoa em anos;
b) a idade dessa pessoa em meses;
c) a idade dessa pessoa em dias;
'''

anoNasc = int(input('DATA DE NASCIMENTO: '))
anoAtual = int(input('ANO ATUAL: '))

anos = anoAtual - anoNasc
print('Idade em anos: {} anos'.format(anos))

meses = anos*12
print('Idade em meses: {} meses'.format(meses))

dias = anos*365
print('Idade em meses: {} dias'.format(dias))
