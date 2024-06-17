'''
Construa um programa que fará o cálculo do salário líquido de um professor. Para fazer esse cálculo, é necessário que sejam lidos o valor da hora aula, o número de horas dadas e o valor total de descontos.

'''
valorHoraAula = float (input('Informe o valor da hora aula: '))
numerosAulas = int(input('informe o número de horas: '))
desconto = float(input('Informe o total de descontos: '))
salarioLiquido = (valorHoraAula*numerosAulas) - desconto

print(f'O valor do salário liquido é:  {salarioLiquido:.2f}')
