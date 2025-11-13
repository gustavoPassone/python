# Exercícios com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável.


def multi(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

calculo = multi(1, 2, 3, 4, 5)
print(calculo)
print(1*2*3*4*5)


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
def par_impar(num):
    verificar = num % 2 == 0
    if verificar:
        return f'{num} é Par'
    return f'{num} é Impar'
        
print(par_impar(1))
print(par_impar(4))