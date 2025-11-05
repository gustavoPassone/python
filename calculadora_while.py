# calculadora com while

while True:
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*)')
    
    numeros_validos = None
    
    try:
        num1_float = 0
        num2_float = 0
        numeros_validos = True
    except Exception as error:
        numeros_validos = None
        
    if numeros_validos is None:
        print('Algum número é inválido')
        continue
    
    operadores_permitidos = '+/*-'

    if operador not in operadores_permitidos:
        print('Operados inválido')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue
    
    ######
    print('---Resultado---')
    if operador == '+':
        print(f'{num1_float} + {num2_float} = {num1_float + num2_float}')
    elif operador == '-':
        print(f'{num1_float} - {num2_float} = {num1_float - num2_float}')
    elif operador == '/':
        print(f'{num1_float} / {num2_float} = {num1_float / num2_float}')
    elif operador == '*':
        print(f'{num1_float} * {num2_float} = {num1_float * num2_float}')
    
    ######
    sair = input('Quer sair? [S]im: ').lower().startswith('s')
    print(sair)
    
    if sair:
        break