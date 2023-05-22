produtos = ('Arroz', 10.00, 'Feijão', 27.75, 
            'Batata', 5.40, 'Macarrão', 8.50)
print('-='*20)
print('{:^30}'.format('LISTAGEM DE PREÇOS'))
print('-='*20)
for produto in range(0, len(produtos)):
    if produto % 2 == 0:
        print(f'{produtos[produto]:.<30}', end=' ')
    else:
        print(f'R$ {produtos[produto]:>6.2f}')