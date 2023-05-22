# As tuplas são Imutáveis
lanche = ('Hamb', 'Suco', 'Pizza', 'Pudim')
# lanche[1] = 'Refrigerante' = Error
# Fatiamento
# print(lanche[-2])
# print(lanche[-4:])
# print(lanche[1:])
# for
for comida in lanche:
    print(f'Eu vou comer ou beber {comida}')
print('Hmmmm...')
#in enumerate
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer ou beber {pos, comida}')
print('Hmmmm...')
# in range
for cont in range(0, len(lanche)):
    print(lanche[cont])
    print(f'Indice: {cont}')
print(f'Quantidade de elementos: {len(lanche)}')
print('FIM')
print(sorted(lanche))
