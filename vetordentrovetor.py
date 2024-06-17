



agenda   = []
nome     = input('Informe nome: ')
idade    = int(input('Informe idade: '))
email    = input('Informe email: ')
endereco = input('Informe endereço: ')
telefone = input('Informe telefone: ')

agenda.append([nome, idade, email, endereco, telefone])

agenda.append(['Maria' , 30 , "Maria@test" , 'Central' ,'222' ])

print(agenda)

print(agenda[0])

#Nome
print(agenda [0] [0])
print(agenda [1] [0])