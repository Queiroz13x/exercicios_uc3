'''
2) Completar o programa, fazendo a leitura em um loop, e sempre perguntando se o 
usuário deseja continuar cadastrando
Ao encerrar a leitura, exibir as pessoas que são menores de idade.
'''


agenda   = []
resp = ''

while True:
    nome     = input('Informe nome: '        )
    idade    = int  (input('Informe idade: '))
    email    = input('Informe email:        ')
    endereco = input('Informe endereço:     ')
    telefone = input('Informe telefone:     ')

    agenda.append([nome, idade, email, endereco, telefone])
    resp = input('Deseja contininuar (S/N)?').lower()
    if resp == 'n':
        break

for contato in agenda:
    if contato[1] <= 18:
        print(contato)