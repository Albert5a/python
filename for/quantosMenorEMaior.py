# Ler ano de nascimento das pessoas e retornar quantas são Maiores e quantas são Menores
from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade < 18:
        totalmenor += 1
    else: 
        totalmaior += 1
print('Temos {} menores de idade e {} maiores de idade!'.format(totalmenor, totalmaior))