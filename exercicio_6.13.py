from cmath import e


temperatura = [-10, -8, 0, 8, 5, 8, 9]
maximo  = temperatura[0]
for x in temperatura:
    if x > maximo:
        maximo = x
print(f'a maior temperatura de mons é {maximo},')
menor  = temperatura[0]
for x in temperatura:
    if x < menor:
        menor = x
print(f'e a menor temperatura é {menor}')
media = menor + maximo / 2
print(media)
