'''
Faça um programa que fará a leitura 
de dois números e o operador
( + - * / )
'''

n1 = int (input('Informe o número: '))
n2 = int (input('Informe outro número: '))
operador = (input('Informe o operador: '))
resultado = 0

match operador: 
    case "+":
        resultado = n1 + n2 
    case "-":
        resultado = n1 - n2
    case "*" | "x" | "X" | "." :
        resultado = n1 * n2
    case "/" | ':':
        if n2 != 0:
            resultado = n1 / n2
    case _:
        print('Operador inválido')
print(f'O resultado é {resultado}')