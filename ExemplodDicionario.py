agenda = []

while True:
    pessoa = {}
    pessoa['nome'    ] = input('Infome nome:        ')
    pessoa['idade'   ] = int(input('Informe a idade:')) 
    pessoa['email'   ] = input('Informe a email:    ')
    pessoa['endereço'] = input('Informe o endereço: ')
    pessoa['telefone'] = input('Informe o telefone: ')

    agenda.append(pessoa)
    r = input('Deseja continuar (S/N) ?' ).lower()
    if r == 'n':
        break

for contato in agenda:
    print(contato['nome'])