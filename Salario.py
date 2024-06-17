'''
Uma empresa concederá um aumento de salário aos seus funcionários, variável de acordo com o cargo,
conforme a tabela abaixo. Faça um algoritimo que leia o salário e o cargo de um funcionário e calcule o
novo salário. Se o cargo do funcinário nao estiver na tabela, ele deverá então, receber 40% de aumento. 
Mostre o salário antigo, o novo salário e a diferença. 
Código Cargo      Percentual 
101    Gerente    10%
102    Engenheiro 20%
103    Técnico    30%
'''

salario = float(input('Informe o codigo: '))
codigo  = int(input('Informe o codigo: '))


novoSalario = 0 

if codigo ==101:
    novoSalario = salario*0.1

elif codigo == 102:
    novoSalario = salario*0.2
elif codigo == 103:
    novoSalario = salario*0.03
else:
    novoSalario = salario*0.4
print('Antigo salário {}, o novo salário {}, o reajuste é de {}'.format(salario,(novoSalario +salario), novoSalario))
