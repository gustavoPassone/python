"""
Listas em Python - Array
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
"""

# print(bool(lista)) # false

lista = [123, True, 'Gustavo', 1.2, []]
print(lista[2])
lista[2] = 'Gustavo MP'
print(lista[2].upper(), type(lista[2]))


lista2 = [10, 20, 30, 40]
print(lista2)

lista2[2] = 300
print(lista2)

del lista2[2]
print(lista2[2])

lista2.append(50)
lista2.append(60)
lista2.append(70)
ultimo_valor = lista2.pop()
print(lista2, 'Removido,', ultimo_valor)

print(20 * '-')

lista3 = [10, 20, 30, 40]
lista3.append('Gustavo')
del lista3[-1]

lista3.insert(0, 5)
print(lista3)