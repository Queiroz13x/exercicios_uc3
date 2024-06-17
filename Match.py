mes = int (input('informe um número:  '))
#if mes == 1 
#    print ('Janeiro')


match mes:
    case 1:
        print('Janeiro')
    case 2:
        print('Fevereiro')
    case 3:
        print('Março')
    case 4:
        print('Abril')
