# lendo 5 pesos e mostrando o maior e o menor peso lido

pesomaior = 0
pesomenor = 0
for pess in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(pess)))
    if pess == 1:
        pesomaior = peso
        pesomenor = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        elif peso < pesomenor:
            pesomenor = peso
print('O maior peso é {}kg e o menor peso é {}kg'.format(pesomaior, pesomenor))

