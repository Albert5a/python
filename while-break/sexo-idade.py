sexo = ''
continuar = ''
maiores = homens = mulheresMenoresVinte = 0 
print('CADASTRANDO PESSOAS')
while True:
    print('-'*30)
    idade = int(input('Qual é sua idade? '))
    while True:
        sexo = str(input('Qual é o seu sexo? [M/F] ').upper())
        if sexo == 'M' or sexo == 'F':
            break
    print('-'*30)
    if idade > 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheresMenoresVinte += 1
    while True:
        continuar = str(input('Deseja continuar? [S/N] ').upper())
        if continuar == 'S' or continuar == 'N':
            break
    if continuar == 'N':
        break
print('-'*30)
print(f'{maiores} pessoas tem mais de 18 anos. {homens} homens cadastrados.')
print(f'{mulheresMenoresVinte} mulheres tem menos de 20 anos')