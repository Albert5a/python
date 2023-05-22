from random import randint
randTupla = (randint(0, 10), randint(0, 10), 
             randint(0, 10), randint(0, 10), 
             randint(0, 10))
print('Os valors sorteados foram: ', end=' ')
for n in randTupla:
    print(f'{n}', end=' ')
randTupla = sorted(randTupla)
menor = randTupla[0]
maior = randTupla[4]
print(f'\nO menor número é {menor} e o MAIOR número é {maior}')
