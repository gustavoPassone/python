"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Gustavo
"""

lista = ['Maria', 'Helena', 'Gustavo']
lista.append('João')
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])