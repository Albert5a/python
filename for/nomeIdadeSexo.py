# LER NOME, IDADE E SEXO. RESPONDER MÉDIA DE IDADE, PESSOA MAIS VELHA E QUANTIDADE DE MULHERES COM MENOS DE 20 ANOS.

mediaIdade = 0
homemVelho = 0
nomeHomemVelho = ''
mulheresMenores = 0
for pess in range (1, 5):
    print('----- {}ª PESSOA -----'.format(pess))
    nome = str(input('Nome: ')).strip()
    idade = float(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    mediaIdade += idade / 4

    if sexo == 'M' and idade > homemVelho:
        homemVelho = idade
        nomeHomemVelho = nome
    if sexo == 'F' and idade < 20:
        mulheresMenores += 1

print('A média de idade do grupo é {} anos.'.format(mediaIdade))
print('O homem mais velhor tem {} anos e se chama {}.'.format(homemVelho, nomeHomemVelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulheresMenores))


    
