"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero = input('Vou dobrar o número que você digitar: ')

try:
    numero = float(numero)
    print(f'O dobro de {numero} é {numero * 2:.2f}')
except:
    print('Isso não é um número')
    
