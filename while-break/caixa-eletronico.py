# print('-'*30)
# print('CAIXA ELETRÔNICO')
# print('-'*30)
# qCedulaUm = qCedulaDez = qCedulaVinte = qCedulaCinquenta = 0
# saque = int(input('Qual será o valor a ser sacado? R$ '))
# print('-'*30)
# restanteSaque = saque
# while True:
#     if restanteSaque < 10:
#         qCedulaUm += restanteSaque
#         restanteSaque = restanteSaque - (qCedulaUm * 1)
#     elif restanteSaque < 20:
#         qCedulaDez = int(restanteSaque / 10)
#         restanteSaque = restanteSaque - (qCedulaDez * 10)
#     elif restanteSaque < 50:
#         qCedulaVinte = int(restanteSaque / 20)
#         restanteSaque = restanteSaque - (qCedulaVinte * 20)
#     else:
#         qCedulaCinquenta = int(restanteSaque / 50)
#         restanteSaque = restanteSaque - (qCedulaCinquenta * 50)
#     if restanteSaque == 0:
#         break
# print(f'Total de {qCedulaCinquenta} cédulas de R$50')
# print(f'Total de {qCedulaVinte} cédulas de R$20')
# print(f'Total de {qCedulaDez} cédulas de R$10')
# print(f'Total de {qCedulaUm} cédulas de R$1')

# Outra forma
print('-'*30)
print('{:^30}'.format('CAIXA ELETRÔNICO'))
print('-'*30)
valor = int(input('Quanto quer sacar: '))
total = valor
cedula = 50
totCedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totCedula += 1
    else:
        if totCedula > 0:
            print(f'Total de {totCedula} cédulas de R$ {cedula:.2f}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totCedula = 0
        if total == 0:
            break
