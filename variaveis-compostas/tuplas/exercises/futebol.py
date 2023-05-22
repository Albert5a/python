times = ('Atletico MG', 'Cruizeiro', 'América', 
         'Palmeiras', 'São Paulo', 'Flamengo', 'Santos', 
         'São Caetano', 'Fluminense', 'Vasco', 'Botafogo', 
         'Avaí', 'Chapecoense', 'Bragantino', 'Ipatinga', 
         'Vila Nova', 'Athletico PR', 'Internacional', 'Grêmio', 
         'Coritiba', 'Fortaleza')
print('-='*60)
print('{:^70}'.format('BRASILEIRÃO'))
print(times)
print('-='*60)
print('{:^70}'.format('1º ao 5º'))
print(f'Os cinco primeiros são: {times[0:5]}')
print('-='*60)
print('{:^70}'.format('Últimos'))
print(f'Os 4 últimos são: {times[16:]}')
print('-='*60)
print('{:^70}'.format('Em ordem Alfabética'))
print(f'{sorted(times)}')
print('-='*60)
print('{:^70}'.format('Colocação da Chapecoense'))
print('Chapecoense está na {}ª posição.'.format(times.index('Chapecoense')))