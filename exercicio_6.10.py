valor1 = [3, 5, 7, 9, 3, 9]
x = 0
primeiroNumero = int(input('informe o primeiro número: '))
segundoNumero = int(input('informe o segundo número: '))
while x < len(valor1):
    if valor1[x] == primeiroNumero:
        break
    x += 1
if primeiroNumero in valor1:
    print(f'1 número: achado na posição {x}')
contador = 0
while contador < len(valor1):
    if valor1[contador] == segundoNumero:
     break    
    contador += 1
if segundoNumero in valor1:
    print(f'2 número: achado na posição {contador}')
else:
    print('nenhum valor encontrado')
 