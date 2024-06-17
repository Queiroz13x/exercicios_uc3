'''
PROFESSOR
Uma empresa concederá um aumento de salário aos seus funcionários, variável de acordo com o cargo,
conforme a tabela abaixo. Faça um algoritimo que leia o salário e o cargo de um funcionário e calcule o
novo salário. Se o cargo do funcinário nao estiver na tabela, ele deverá então, receber 40% de aumento. 
Mostre o salário antigo, o novo salário e a diferença. 
Código Cargo      Percentual 
101    Gerente    10%
102    Engenheiro 20%
103    Técnico    30%
'''

salario = float(input('Informe o salário: '))
cargo = int(input('Informe o cargo: '))
novoSalario = 0
diferença  = 0
if cargo == 101:
    diferença = salario * 0.1
elif cargo == 102:
    diferença = salario * 0.3
else:
    diferença = salario * 0.4
novoSalario = salario + diferença
print(f'Sala: {salario:2f}\n diferença: {diferença:.2f}')
print(f'Novo Salário: {novoSalario:.2f}')