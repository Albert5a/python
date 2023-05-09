# maiores = homens = mulheresMenoresVinte = 0 
# print('CADASTRANDO PESSOAS')
# while True:
#     print('-'*30)
#     idade = int(input('Qual é sua idade? '))
#     while True:
#         sexo = str(input('Qual é o seu sexo? [M/F] ').upper())
#         if sexo == 'M' or sexo == 'F':
#             break
#     print('-'*30)
#     if idade >= 18:
#         maiores += 1
#     if sexo == 'M':
#         homens += 1
#     elif sexo == 'F' and idade < 20:
#         mulheresMenoresVinte += 1
#     while True:
#         continuar = str(input('Deseja continuar? [S/N] ').upper())
#         if continuar == 'S' or continuar == 'N':
#             break
#     if continuar == 'N':
#         break
# print('-'*30)
# print(f'{maiores} pessoas é maior de idade. {homens} homens cadastrados.')
# print(f'{mulheresMenoresVinte} mulheres tem menos de 20 anos')

# outra forma
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{tot18} pessoas é maior de idade. {totH} homens cadastrados.')
print(f'{totM20} mulheres tem menos de 20 anos')
