valorUm = int(input('Digite um número: '))
valorDois = int(input('Digite um número: '))
valorTres = int(input('Digite um número: '))
valorQuatro = int(input('Digite um número: '))
tupla = (valorUm, valorDois, valorTres, valorQuatro)
print(f'Você digitou {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares foram:', end=' ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
