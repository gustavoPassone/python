"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd de caracteres da str
"""

variavel = 'Hello World'
print(variavel[4:])
print(variavel[4:8])
print(variavel[:4])
print(10 * '-')
print(len(variavel))
print(10 * '-')
print(variavel[0:10:2])
print(variavel[::-1]) # inverter