"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')

# lista_produtos = []

# while True:
#     print('Selecione uma opção')
#     opcao_selecionada = input('[i]nserir [a]pagar [l]istar: ')

#     if len(opcao_selecionada) > 1:
#         print('Digite apenas uma letra')
#         continue
    
#     if opcao_selecionada == 'i':
#         novo_item = input('Digite o item que deseja adicionar: ')
#         lista_produtos.append(novo_item)
#         continue
    
#     elif opcao_selecionada == 'a':
#         indice_apagar = int(input('Escolha o índice para apagar: '))
#         del lista_produtos[indice_apagar]
#         continue
    
#     elif opcao_selecionada == 'l':
#         for i, n in enumerate(lista_produtos):
#             if len(lista_produtos) < 1:
#                 print('Nada para listar')
#                 continue
#             else:
#                 print(i, n)
#                 continue