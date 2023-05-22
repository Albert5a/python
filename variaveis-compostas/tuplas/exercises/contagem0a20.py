numbers = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 
           'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 
           'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 
           'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 
           'Dezenove', 'Vinte')
escolha = 21
while escolha not in range(0, len(numbers)):
    escolha = int(input('Digite um número entre 0 e 20: '))
    if escolha in range(0, len(numbers)):
        print(f'Você digitou {numbers[escolha]}')
        repete = ' '
        while repete not in 'SN':
            while True:
                repete = str(input('Quer outro número? [s/n] ')).strip().upper()
                if repete == 'S':
                    escolha = int(input('Digite um número entre 0 e 20: '))
                    print(f'Você digitou {numbers[escolha]}')
                else:
                    break
print('FIM')


# Outra forma
# numbers = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 
#            'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 
#            'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 
#            'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 
#            'Dezenove', 'Vinte')
# while True:
#     escolha = int(input('Digite um número entre 0 e 20: '))
#     if 0 <= escolha <= 20:
#         break
#     print('Tente novamente.', end=' ')
# print(f'Você digitou {numbers[escolha]}')
