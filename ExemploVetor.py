'''
1) Faça um programa que fará a leitura de indeterminados números e esses números serão armazenados 
em um vetor.
Quando o usuário digitar 0, o programa interromperá a leitura e irá imprimir o
somatório dos números e a quantidade de elementos
'''

vetor = []

#Entrada
while True:
    numero = int(input('Informe o número: '))
    vetor.append(numero)
    if numero == 0:
        break

#Procesamento
soma = 0 
for n in vetor:
    soma+=numero 

#Saida
print(f'A soma dos elementos é {soma}')
print(f'A quantidade de elementos: {len(vetor)}')

print(f'Utilizando a função sum {sum(vetor)} ')

#vetor.pop() - Elimina a ultima posição do vetor, colocar fora do while 