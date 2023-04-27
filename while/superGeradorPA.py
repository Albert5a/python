print('Gerador de PA')
primeiro = int(input('Primeiro termo PA: '))
razao = int(input('Qual é a razão da PA: '))
termo = primeiro
contador = 1
limiteContador = 10
while contador <= limiteContador:
    print('{} => '.format(termo), end='')
    termo += razao
    contador += 1
    if contador > limiteContador:
        print('PAUSA')
        maisTermos = int(input('Quantos termos você quer ver a mais: '))
        if maisTermos > 0:
            limiteContador += maisTermos
print('Progressão finalizada com {} termos mostrados'.format(limiteContador))

# Versão do professor
# print('Gerador de PA')
# primeiro = int(input('Primeiro termo PA: '))
# razao = int(input('Qual é a razão da PA: '))
# termo = primeiro
# contador = 1
# total = 0
# mais = 10
# while mais != 0:
#     total = total + mais
#     while contador <= total:
#         print('{} => '.format(termo), end='')
#         termo += razao
#         contador += 1
#     print('PAUSA')
#     mais = int(input('Quantos termos você quer mostrar a mais? '))
# print('Com {} termos mostrados.'.format(total))