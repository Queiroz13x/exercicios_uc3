'''
Faça um programa fará a leitura de uma temperatura em graus Kelvin e apresentá-la em graus Celsius.
A fórmula da conversão é C = K - 273.15323
'''

kelvin = float(input('Informe a temperatura em Kelvin: '))



celsius = kelvin - 273.15323
print (f'A  temperatura em celsius é : {celsius:.2f}ºc')
