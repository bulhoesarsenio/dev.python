array = []
x = 0
while True:
    valor = int(input('digite um número (-1 para sair): '))
    if valor == -1:
        break
    array.append(valor)
    
for iterador in array:
    #x = x + 1
    print(f'{x}: {iterador}')
    x = x + 1