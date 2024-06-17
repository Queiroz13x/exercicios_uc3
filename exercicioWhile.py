



r = ''
quantidadesalario= 0
quantidadefilhos = 0 
quant = 0 

while True:
    nome= (input('Informe nome: '))
    quantidadesalario +=1
    salarios = float(input('informe o seu salário: '))
    quantidadesalario += salarios 
    filho = int (input('Informe a quantidade de filhos: '))
    quantidadefilhos += filho 
    r=input('Deseja continuar?(S/N) ')
    if r.lower()== 'n':
        break
print(f'A média salarial do município é de R$ {salarios/quantidadesalario:.2f} e a média de filhos é de {quantidadefilhos/filho:.2f}')