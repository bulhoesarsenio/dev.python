L = [8, 9, 3, 2, 43, 78, 98, 54]
valor1 = int(input('(p): digite o valor a procurar: '))
valor2 = int(input('(v): digite o valor a procurar: '))
if valor1 in L:
    print(f'valor1: {valor1} encontrado')
else:
    print(f'valor1: {valor1} não encontrado')
if valor2 in L:
    print(f'valor2: {valor2} encontrado')
else:
    print(f'valor2: {valor2} não encontrado')
if valor1 in L:
    print('(valor1) foi achado primeiro')
elif valor2 in L:    
    print('(valor2) foi achado primeiro') 