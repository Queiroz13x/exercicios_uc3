'''
FAÇA UM PROGRAMA QUE CONVERTA UMA TEMPERATURA EM CELSIUS PARA FAHRENHEIT UTILIZANDO A FÓRMULA ABAIXO:

F = 9C / 5 + 32 

'''
celsius = float (input( "INFORME A TEMPERATURA EM CELSIUS: "))
fahrenheit = 9 * celsius / 5 + 32

print(f'A temperatura é {fahrenheit:.2f}')