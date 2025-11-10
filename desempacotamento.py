"""
Introdução ao empacotamento e desempacotamento
"""

# nome1, nome2, nome3 = ['Maria', 'Helena', 'Gustavo']

_, nome2, *_ = ['Maria', 'Helena', 'Gustavo'] # _ serve para dizer que não valor usar a variavel
print(nome2, _)