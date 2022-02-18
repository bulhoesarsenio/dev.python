nome = str(input('INFORME SEU NOME: '))
print('=' * 30)
nome_maiusculo = (nome.upper())
print(f'ÓLA {nome_maiusculo}! SEJA BEM-VINDO AO BANCO DO BARSIL')
print('=' * 30)
valor = int(input(f'{nome_maiusculo} quantas cédulas você quer sacar? r$: '))
total = valor
cedulas = 100
total_cedulas = 0
while total <= 1000:
    if total >= cedulas:
        total -= cedulas
        total_cedulas += 1 
    else:
       if total_cedulas > 0:
           print(f'você receberá um total de {total_cedulas} cédulas de r${cedulas}')
       if cedulas == 100:
           cedulas = 50
       elif cedulas == 50:
          cedulas = 20
       elif cedulas == 20:
          cedulas = 10
       elif cedulas == 10:
          cedulas = 5
       elif cedulas == 5:
          cedulas = 1
       total_cedulas = 0
       if total == 0:
         break
if total > 1000:
    print('valor inválido! você só pode sacar um valor igual a 1000 ou um valor menor quê 1000')
print('=' * 30)
print(f'{nome_maiusculo} VOLTE SEMPRE AO BANCO DO BRASIL')