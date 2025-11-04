# operadores in e not in
# string são iteráveis

nome = 'Gustavo'
print(nome[2])

print('a' in nome) # true
print('z' in nome) # false
print(10 * '-')
print('Gus' not in nome)
print(10 * '-')
nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
    