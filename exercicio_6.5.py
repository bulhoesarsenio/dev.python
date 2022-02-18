último = 10
fila = list(range(1, último+1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print("Fila atual:", fila)
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair,")
    print('ou você pode digitar varios comandos exemplos: fffff ou aaaaaa')
    
    operação = input("Operação (F, A ou S):")
    x = 0
    sair = False
    while x < len(operação):
        if operação[x] == "A" or operação[x] == 'a':
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operação[x] == "F" or operação[x] == 'f':
            último += 1
            fila.append(último)
        elif operação[x] == "S":
            sair = True
            print(operação.upper)
            print(operação.lower)
            break
            

        else:
            print(f"Operação inválida: {operação[x]} na posição {x}! Digite apenas F, A ou S!")
        x = x + 1
    if sair:
        break
    