contador = 0
primeira = []
segunda = []
terceira = []
quarta = []
lista1 = []
lista2 = []
cont = 0
while True:
    
    lista1 = int(input(f"Digite para a posição {contador} da primeira lista (0 para terminar): "))
    contador = contador + 1
    if lista1 == 0:
        break
    primeira.append(lista1)
while True:
    lista2 = int(input(f"Digite para a posição {cont} da segunda lista (0 para terminar): "))
    cont = cont + 1 
    if lista2 == 0:
        break
    segunda.append(lista2)
        
duas_listas = primeira[:]
duas_listas.extend(segunda)
x = 0
while x < len(duas_listas):
    valor = 0
    while valor < len(terceira):
        if duas_listas[x] == terceira[valor]:
            break
        valor = valor + 1
    if valor == len(terceira):
        terceira.append(duas_listas[x])
    x = x + 1
x = 0
while x < len(terceira):
    print(f"{x}: {terceira[x]}")
    x = x + 1