valores = [5, 7, 9, 1, 87, 65]
x = 0
procurando = int(input('digite o valor a procurar: '))
while x < len(valores):
    if valores[x] == procurando:
     break
    x = x + 1
print(valores)
if procurando in valores:
    print(f'{procurando} achado na posição {x}')
else:
    print(f'{procurando} não achado')
