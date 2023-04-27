numberEnter = int(input('Digite um número [999 para parar]: '))
sumNumber = c = 0
while numberEnter != 999:
    sumNumber += numberEnter
    c += 1
    numberEnter = int(input('Digite um número [999 para parar]: '))
print('Foram digitados {} números e a soma deles é igual a {}'.format(c, sumNumber))

