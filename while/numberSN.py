number = int(input('Digite um número: '))
sumNumber = number
c = 1
wantToContinue = str(input('Quer continuar? [S/N] ').upper())
heighestValue = lowerValue = number
while wantToContinue == 'S':
    number = int(input('Digite um número: '))
    sumNumber += number
    c += 1
    wantToContinue = str(input('Quer continuar? [S/N] ').upper())
    if number > heighestValue:
        heighestValue = number
    elif number < lowerValue:
        lowerValue = number
average = sumNumber / c
print('Foram digitados {} números e a média deles é igual a {}'.format(c, average))
print('O maior valor foi {} e o menor foi {}'.format(heighestValue, lowerValue))

# Professor
# resp = 'S'
# soma = quant = media = maior = menor = 0
# while resp in 'Ss':
#     num = int(input('Digite um número: '))
#     soma += num
#     quant += 1
#     if quant == 1:
#         maior = menor = num
#     else:
#         if num > maior:
#             maior = num
#         if num < menor:
#             menor = num
#     resp = str(input('Quer continuar? [S/N] '))
# media = soma / quant
# print('Você digitou {} números e a média foi {}'.format(quant, media))
# print('O maior valor foi {} e o menor foi {}'.format(maior, menor))