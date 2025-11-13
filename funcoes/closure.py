"""
Closure e funções que retornam outras funções
"""

def calculator(number1: int | float, number2: int | float):
    def calculation_type(operator):
        operators: dict[str, int | float] = {'+': number1 + number2,
                                             '-': number1 - number2,
                                             '*': number1 * number2,
                                             '/': number1 / number2}
        try:
            return round(operators[operator], 2)
        except ZeroDivisionError:
            return 'Não é possivel dividir por zero'
        except KeyError:
            return f'O "{operator}" operador não existe.'
    return calculation_type
 
 
operation = calculator(1, 1)
 
print(operation('+'))  # 2
print(operation('-'))  # 0
print(operation('*'))  # 1
print(operation('/'))  # 1 


# -------

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))