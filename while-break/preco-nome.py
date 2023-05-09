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
    if precoMaisBarato == 0 or preco < precoMaisBarato:
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
print(f'O produto mais barato foi {nomeMaisBarato}')

# Outra forma
# total = totMil = menor = cont = 0
# barato = ''
# while True:
#     produto = str(input('Produto: '))
#     preco = float(input('Preço: '))
#     cont += 1
#     total += preco
#     if preco > 1000:
#         totMil += 1
#     if cont == 1 or preco < menor:
#         menor = preco
#         barato = produto
#     resp = ' '
#     while resp not in 'SN':
#         resp = str(input('Quer continuar com [S/N]: ')).strip().upper()[0]
#     if resp =='N':
#         break
# print('{:^40}'.format('FIM DO PROGRAM'))
# print(f'O total foi: R$ {preco:.2f}')
# print(f'{totMil} custam mais de R$ 1000.00')
# print(f'O mais barato foi: {barato} e custa R$ {menor:.2f}')