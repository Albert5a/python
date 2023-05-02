while True:
    print('-'*60)
    num = int(input('Escolhe um número para ver sua tabuada: (Negativo para parar) '))
    print('-'*60)
    cont = 0
    if num < 0:
        break
    while cont < 10:
        cont += 1
        result = num * cont
        print(f'{num} * {cont} = {result}')
print('Você digitou um número negativo. FIM!')

# outra forma
# while True:
#     n = int(input('Quer ver a tabuada de qual valor? '))
#     if n < 0:
#         break
#     for c in range(1, 11):
#         print(f'{n} x {c} = {n*c}')
# print('Programa encerrado')
