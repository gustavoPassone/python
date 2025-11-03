nome = 'Gustavo'
altura = 1.75
peso = 60
imc = peso / (altura ** 2)

# f-strings
mensagem = f'{nome} seu IMC é: {imc:.2f}' # :.2f é para formatar as casas decimais

print(mensagem)