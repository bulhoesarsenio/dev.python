from ast import If


senhaDaContaOrigem = 0
senhaDaContaDestino  = 0
depositando = 0
valorTransferencia = 0
numeroConta1 = 8888
numeroConta2 = 9999
senhaConta1 = 1111 
senhaConta2 = 2222 
saldoCliente1 = 800
saldoCliente2 = 12
print('1_SACAR')
print('2_TRANSFERÊNCIA')
print('3_SALDO')
print('4_DEPÓSITAR')
print('5_SAIR')
while True:
    opcao = int(input('QUAL OPERAÇÃO VOCÊ DESEJA EXECULTAR: '))
    if opcao == 1:
        contaDoSaque = int(input('INFORME A O NÚMERO DA SUA CONTA: '))
        if contaDoSaque == numeroConta1:
            senhaDOsaque = int(input('INFORME A SENHA DA CONTA: '))
            if senhaDOsaque == senhaConta1:
                print('CLIENTE AUTENTICADO COM SUCESSO')
                valorDoSaque = float(input('INFORME O VALOR DO SAQUE: '))
                if valorDoSaque <= saldoCliente1:
                    print('SAQUE REALIZADO COM SUCESSO')
                    print(f'VOCÊ FEZ UM SAQUE DE R${valorDoSaque} DA CONTA1')
                elif valorDoSaque > saldoCliente1:
                    print('SALDO INSUFICIENTE! VOCÊ NÃO TEM ESSE VALOR')
            else:
                print('SENHA INVÁLIDA')
        if contaDoSaque == numeroConta2:
            print('conta correta')
            if senhaDOsaque == senhaConta2:
                print('CLIENTE AUTENTICADO COM SUCESSO')






""""    
    elif opcao == 2:
        numeroConta = int(input('INFORME O NÚMERO DA SUA CONTA: '))
        if numeroConta == numeroConta1:
            senhaConta = int(input('INFORME A SENHA DA CONTA: '))
            if senhaConta == senhaConta1:
                print('CLIENTE AUTENTICADO COM SUCESSO, SEJA BEM VINDO!')
                valorTransferencia = float(input('INFORME O VALOR A SER TRANSFERIDO: '))
                if valorTransferencia <= saldoCliente1:
                    saldoCliente1 = saldoCliente1 - valorTransferencia
                    saldoCliente2 = saldoCliente2 + valorTransferencia
                    print(f'FOI TRANSFERIDO {valorTransferencia}')
                    print(f'O SALDO DO CLIENTE 1 É DE {saldoCliente1}')
                    print(f'O NOVO SALDO DO CLIENTE 2 É DE {saldoCliente2}')
                elif valorTransferencia > saldoCliente1:
                    print('SALDO EM CONTA INFERIOR AO VALOR SOLICITADO.')
            else:
                print('A SENHA INFORMADA É INVÁLIDA.')
        elif numeroConta == numeroConta2:
            print('OK, ESTOU NO ELIF...')
        else:
            print('ESTOU NO ELSE, NADA ACONTECEU ANTES....')
"""