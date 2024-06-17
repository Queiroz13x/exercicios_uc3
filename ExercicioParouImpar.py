'''
Faça um programa que peça 10 números inteiros, 
calcule e mostre a quantidade de números pares 
e a quantidade de números impares.
'''

impar=0
par = 0
for numero in range(10):
    n = int(input('informe o número: '))
    if n % 2 == 0:
        par += 1 
    else:
        impar += 1
print(f'Quantidade número de pares: {par}')
print(f'Quantidade número de impares: {impar}')