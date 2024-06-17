'''
FAÇA UM PROGRAMA FARÁ A LEITURA DE UMA TEMPERATURA EM GRAUS FAHRENHEIT E APRESENTÁ-LA EM GRAUS CELSIUS. 
A FÓRMULA DA CONVERSÃO É C = 5 * (F - 32) /9 

'''
fahrenheit = float(input('Informe a temperatura em Fahrenheit: '))
celsius =  5*(fahrenheit - 32) / 9 
print (f'A  temperatura é: {celsius:.2f}')