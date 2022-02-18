while True:
    conta1 = int(input('INFORME O NÚMERO DA CONTA1: '))
    conta2 = int(input('INFORME O NÚMERO DA CONTA2: '))
    if conta1 != conta2:
        senha1 = int(input('INFORME A SENHA DA CONTA1: '))
        senha2 = int(input('INFORME A SENHA DA CONTA2: '))
        if senha1 != senha2 and senha1 and senha2 != conta1 and conta2:
            break
senhaDaContaOrigem = 0
senhaDaContaDestino  = 0
valorDoDeposito = 0
valorTransferencia = 0
numeroConta1 = conta1
numeroConta2 = conta2
senhaConta1 = senha1 
senhaConta2 = senha2 
saldoCliente1 = 800
arquivo = 0
saldoCliente2 = 12
print('1_SACAR')
print('2_TRANSFERÊNCIA')
print('3_SALDO')
print('4_DEPÓSITAR')
print('5_SAIR')
while True:
    opcao = int(input('QUAL OPERAÇÃO VOCÊ DESEJA EXECULTAR: '))
    if opcao == 1:
        numeroConta  = int(input('INFORME O NÚMERO DA SUA CONTA: '))
        if numeroConta == numeroConta1:
            senhaConta = int(input('INFORME A SENHA DA CONTA: '))
            if senhaConta == senhaConta1:
                print('CLIENTE AUTENTICADO COM SUCESSO, SEJA BEM VINDO!')
                valorSaque = int(input('INFORME O VALOR DO SAQUE: '))
                if valorSaque <= saldoCliente1:
                    saldoCliente1 = saldoCliente1 - valorSaque
                    print(f'FOI REALIZADO UM SAQUE DE {valorSaque}')
                    print(f'O SALDO DO CLIENTE 1 É DE {saldoCliente1}')
                    print(F'O SALDO DO CLIENTE 2 É DE {saldoCliente2}  ')
                elif valorSaque > saldoCliente1:
                    print('IMPOSSÍVEL REALIZAR O SAQUE, SALDO INSUFICIENTE.')
            if numeroConta != numeroConta1 and numeroConta2:
                print('CONTA INVÁLIDA')            
            else:
                print('A SENHA INFORMADA É INVÁLIDA.')
        if numeroConta == numeroConta2:
            senhaConta = int(input('INFORME A SENHA DA CONTA: '))
            if senhaConta == senhaConta2:
                print('CLIENTE AUTENTICADO COM SUCESSO, SEJA BEM VINDO!')
                valorSaque = float(input('INFORME O VALOR DO SAQUE: '))
                if valorSaque <= saldoCliente2:
                    saldoCliente2 = saldoCliente2 - valorSaque
                    print(f'FOI REALIZADO UM SAQUE DE {valorSaque}')
                    print(f'O SALDO DO CLIENTE 2 É DE {saldoCliente2}')
            elif valorSaque > saldoCliente2:
                print('IMPOSSÍVEL REALIZAR O SAQUE, SALDO INSUFICIENTE.')
            else:
                print('A SENHA INFORMADA É INVÁLIDA.')
    if opcao == 2:
        senhaConta = int(input('INFORME O NÚMERO DA SUA CONTA: '))
        if senhaConta == numeroConta1:
            numeroConta = int(input('INFORME A SENHA DA CONTA: '))
            if numeroConta == senhaConta1:
                print('CLIENTE AUTENTICADO COM SUCESSO, SEJA BEM VINDO!')
                valorTransferencia = float(input('INFORME O VALOR A SER TRANSFERIDO: '))
                if valorTransferencia <= saldoCliente1:
                    saldoCliente1 = saldoCliente1 - valorTransferencia
                    saldoCliente2 = saldoCliente2 + valorTransferencia
                    print(f'FOI TRANSFERIDO {valorTransferencia}')
                    print(f'O SALDO DO CLIENTE 1 É DE {saldoCliente1}')
                    print(f'O NOVO SALDO DO CLIENTE 2 É DE {saldoCliente2}')
                elif valorTransferencia > saldoCliente1:
                    print('SALDO INSUFICIENTE.')
                elif senhaConta != numeroConta1 or senhaConta != numeroConta2:
                    print('conta inválida')
            else:
                print('SENHA NÃO AUTENTICADO')
        if senhaConta == numeroConta2:
            numeroConta = int(input('INFORME A SENHA DA CONTA: '))
            if numeroConta == senhaConta2:
                print('CLIENTE AUTENTICADO COM SUCESSO, SEJA BEM VINDO!')
                valorTransferencia = float(input('INFORME O VALOR A SER TRANSFERIDO: '))
                if valorTransferencia <= saldoCliente2:
                    saldoCliente2 = saldoCliente2 - valorTransferencia
                    saldoCliente1 = saldoCliente1 + valorTransferencia
                    print(f'FOI TRANSFERIDO {valorTransferencia}')
                    print(f'O SALDO DO CLIENTE 2 É DE {saldoCliente2}')
                    print(f'O NOVO SALDO DO CLIENTE 1 É DE {saldoCliente1}')
                elif valorTransferencia > saldoCliente2:
                    print('SALDO INSUFICIENTE. TRANSFERÊNCIA NÃO REALIZADA')
            else:
                print('cliente não autenticado')
    if opcao == 3:
        saldoDconta = int(input('INFORME O NÚMERO DA CONTA QUE VOCÊ QUER SABER O SALDO: '))
        if saldoDconta == numeroConta1:
            print(f'O SALDO DO CLIENTE 1 É DE r${saldoCliente1}')
        elif saldoDconta == numeroConta2:
            print(f'O SALDO DO CLIENTE 2 É DE r${saldoCliente2}')
        else:
            print('conta inexistente')
    if opcao == 4:
        contaDoDeposito = int(input('INFORME O NÚMERO DA CONTA QUE VOCÊ QUER FAZER O DEPÓSITO: '))
        valorDoDeposito = int(input('INFORME O VALOR DO DEPÓSITO: '))
        if contaDoDeposito == numeroConta1:
            saldoCliente1 = saldoCliente1 + valorDoDeposito
            print(f'VOCÊ DEPÓSITOU R${valorDoDeposito} PARA A CONTA 1')
        elif contaDoDeposito == numeroConta2:
             saldoCliente2 = saldoCliente2 + valorDoDeposito
             print(f'VOCÊ DEPÓSITOU R${valorDoDeposito} PARA A CONTA 2')
        elif contaDoDeposito != numeroConta1 or contaDoDeposito != numeroConta2:
            print('CONTA INVÁLIDA')
    if opcao == 5:
        break
    