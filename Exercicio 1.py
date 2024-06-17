print('FINALIZAÇÃO DE PAGAMENTO')

valorTotal = float(input('INFORME O VALOR TOTAL DA COMPRA: '))
numeroParcelas =  int(input('Informe um número de parcelas:' ))

valorParcela = valorTotal / numeroParcelas
print(f'por parcelas {valorParcela:.2f}')
 