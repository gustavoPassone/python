# Operadores lógicos
# or
# or - Qualquer condição verdadeira avalia toda a expressão como verdadeira. Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor.
# São considerados falsy

entrada = input('[E] Entrar [S] Sair: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
    
senha = input('Senha: ') or 'Sem senha'
print(senha)