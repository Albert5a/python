produtos = ('Arroz', 10.00, 'Feijão', 27.75, 'Batata', 5.40, 'Macarrão', 8.50)
print('-='*20)
print('{:^30}'.format('LISTAGEM DE PREÇOS'))
print('-='*20)
print('{:.<30}'.format(produtos[0]), end=' ')
print(f'R$ {produtos[1]:>6.2f}')
print('{:.<30}'.format(produtos[2]), end=' ')
print(f'R$ {produtos[3]:>6.2f}')
print('{:.<30}'.format(produtos[4]), end=' ')
print(f'R$ {produtos[5]:>6.2f}')
print('{:.<30}'.format(produtos[6]), end=' ')
print(f'R$ {produtos[7]:>6.2f}')
print('-='*20)
