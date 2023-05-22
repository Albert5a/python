valores = []
valores.append(1)
valores.append(3)
valores.append(5)

for cont in range(3, 5):
    valores.append(int(input('Digite um valor: ')))

for x, y in enumerate(valores):
    print(f'No índice {x} temos o valor {y}')
print('Fim da lista!')