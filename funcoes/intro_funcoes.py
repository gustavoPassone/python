"""
DEF
elas podem receber valores para parâmetros (argumentos) e retornar um valor especifico
por padrão, funções Python retornam None (nada)
"""

def imprimir(a, b, c):
    print(a, b, c)
    
imprimir(1, 2, 3)
imprimir(4, 5, 6)

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}')
    
saudacao('Gustavo')
saudacao('Maria')
saudacao()