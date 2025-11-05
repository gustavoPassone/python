num = input('Digite um número inteiro: ')

try:
    num_int = int(num)
    if num_int % 2 == 0:
        print('Número par')
    else:
        print('Número impar')
except:
    print('Digite um número')
    
print(10 * '-')
    
hora = input('Digite a hora: ')

try:
    hora_int = int(hora)
    
    if hora_int >= 0 and hora_int <= 11:
        print('Bom dia')
    elif hora_int >= 12 and hora_int <= 17:
        print('Boa tarde')
    elif hora_int >=18 and hora_int <= 23:
        print('Boa noite')
    else:
        print('Digite uma hora válida')
except:
    print('Digite apenas números inteiros')

print(10 * '-')

nome = input('Digite seu nome: ')

if len(nome) >= 4:
    print('Nome curto')
elif len(nome) > 4 and len(nome) <=6:
    print('Nome normal')
else:
    print('Nome grande')