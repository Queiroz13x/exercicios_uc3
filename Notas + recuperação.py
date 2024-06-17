'''
Faça um programa que fará a leitura de duas notas e irá calcular a média. 
Se a média for maior ou igual a 7, o programa irá escrever "aprovado",
Se não o programa irá pedir a nota de recuperação, e fará um novo cálculo da média
envolvendo a média com a recuperação.
Se a nova média for maior ou igual a 6, o programa escreverá 'Aprovado' senão, escreverá "Reprovado".
'''

nota1 = float (input('NOTA 1: '))
nota2 = float (input('NOTA 2: '))
media = nota1 + nota2 / 2 
recuperacao = 0 

if media >= 7:
   print('APROVADO')

elif media <=7
  input('Nota de recuperação: ')

#elif idade >=13 and idade <=13:
   #print('Juvenil A ')


else:
    print('Categoria inválida')