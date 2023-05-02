print('-'*30)
print('O que você vai comprar?')
print('-'*30)
total = maisDeMil = precoMaisBarato = 0
nomeMaisBarato = ''
contador = 0
while True:
    nome = str(input('Qual é o produto? '))
    preco = float(input('Qual é o preço? '))
    print('-'*30)
    total += preco
    if precoMaisBarato == 0:
        precoMaisBarato = preco
        nomeMaisBarato = nome
    elif preco < precoMaisBarato:
        precoMaisBarato = preco
        nomeMaisBarato = nome
    if preco > 1000:
        maisDeMil += 1
    continuar = str(input('Deseja continuar? ').upper())
    print('-'*30)
    while True:
        if continuar == 'S' or continuar == 'N':
            break
    if continuar == 'N':
        break
print(f'O valor total da compra foi R${total:.2f}')
print(f'{maisDeMil} produtos custam mais de R$1000,00')
print(f'O broduto mais barato foi {nomeMaisBarato}')
