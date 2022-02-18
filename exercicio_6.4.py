ultimo = 10
fila = list(range(1, ultimo + 1))
while True:
    print(f'\n \033[4;32;36mEXISTEM {len(fila)} CLIENTES NA FILA')
    print(f'FILA ATUAL: {fila}')
    print('DIGITE (F) PARA ADICIONAR UM ELEMENTO AO FIM  DA FILA,')
    print('OU (A) PARA REALIZAR O ATENDIMENTO. (S) PARA SAIR')
    operacao = input('OPERAÇÃO (F, A ou S): ')
    if operacao == 'a' or operacao == 'A':
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f'\033[4;32;36mclientes {atendido} atendido(s)')
        else:
            print('fila vazia! ninguém para atender')
            
    elif operacao == 'f' or operacao == 'F':
        ultimo += 1
        fila.append(ultimo)
    elif operacao == 's' or operacao == 'S':
        break
    else:
        print('operação inválida! digite f, a ou s!')