valorUm = int(input('Digite um número: '))
valorDois = int(input('Digite um número: '))
valorTres = int(input('Digite um número: '))
valorQuatro = int(input('Digite um número: '))
tupla = (valorUm, valorDois, valorTres, valorQuatro)
print(f'Você digitou {tupla}')
if 9 in tupla:
    print(f'O número 9 aparece {tupla.count(9)} vezes')
else:
    print('Não temos número 9 na tupla')
if 3 in tupla:
    print(f'O primeiro 3 aparece na {(tupla.index(3)) + 1}ª posição')
else:
    print('Não temos número 3 na tupla')
for c in tupla:
    if c % 2 == 0:
        print(c)
