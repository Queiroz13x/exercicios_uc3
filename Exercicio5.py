'''
Faça um programa que calcula e apresente o valor do volume de um recipiente, utilizando a fórmula 
volume = 3.14159 * raio * raio * altura

'''

raio =  float (input('Informe o raio: '))
altura = float (input('Informe a altura: '))

volume = 3.14159 * raio * raio * altura
print(f'O volume é {volume:.2f}')

volume = 3.14159 * raio ** 2 * altura
print(f'O volume é {volume:.2f}')
