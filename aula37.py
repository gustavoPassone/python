contador = 1

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não mostra o 6')
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue
    
    print(contador)
    
    
print('Acabou')