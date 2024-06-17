#Vetor - Conjunto - Array - Lista 

vetor = []              #Declarando o vetor 
vetor.append('Leandro') #Adicionando elementos
vetor.append('Vilma')
vetor.append('Joana')
print(vetor)
print(vetor[0])         # 0 é a primeira posição do vetor 

vetor.append(input('Informe o nome:'))

print(vetor)

#'len' retorna o número de elementos de um vetor

print(len(vetor))

for nome in vetor: 
    print(nome)
