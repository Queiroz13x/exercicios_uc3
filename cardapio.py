'''
O cardápio de uma lanchonete é o seguinte:
Especificação    Código       Preço
Cachorro quente   100          1,20
Bauru simples     101          1,30
Bauru com ovo     102          1,50
Hambúrger         103          1,20
Cheeseburguer     104          1,30
Refrigerante      105          1,00
    Escrever um algoritmo que leia o código do item pedido, 
a quantidade e calcule o valor a ser pago por aquele lanche.
Considere que a cada execução somente será calculado um item
'''

itemPedido = int(input('Insira o codigo de lanche: '))
quantidade = int(input('Digite a quantidade: '))

if itemPedido   == 100:
   print('Valor total - Cachorro Quente - R$ {:.2f}'.format(quantidade*1.20))
elif itemPedido == 101:
   print('Valor total - Bauru Simples - R$ {:.2f}'.format(quantidade*1.30)) 
elif itemPedido == 102:  
   print('Valor total - Bauru com Ovo - R$ {:.2f}'.format(quantidade*1.50))
elif itemPedido == 103:  
   print('Valor total - Hambúrguer - R$ {:.2f}'.format(quantidade*1.20))
elif itemPedido == 104:  
   print('Valor total - Cheeseburguer - R$ {:.2f}'.format(quantidade*1.30))
elif itemPedido == 105:
   print('Valor total - Refrigerante - R$ {:.2f}'.format(quantidade*1.00))