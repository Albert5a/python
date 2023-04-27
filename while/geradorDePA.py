print('Gerador de PA')
primeiro = int(input('Primeiro termo PA: '))
razao = int(input('Qual é a razão da PA: '))
termo = primeiro
contador = 1
while contador <= 10:
    print('{} '.format(termo), end='')
    print('=> ' if contador < 10 else '... ', end='')
    termo += razao
    contador += 1
print('FIM')
