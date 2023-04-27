# from math import factorial
# n = int(input('Digite um número para calcular o fatorial: '))
# f = factorial(n)
# print('O fatorial de {} é {}'.format(n, f))

##################################################################

# Modo tradicional
num = int(input('Escolha um número para calcular o fatorial: '))
c = num
fatorial = 1
while c >= 1:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    fatorial *= c
    c -= 1
print('O fatorial de {} é {}'.format(num, fatorial))

##################################################################

# num = int(input('Escolha um número para calcular o fatorial: '))
# fatorial = 1
# for i in range (1, num + 1):
#     print('{}'.format(i), end=' ')
#     print(' x ' if i < num else ' = ', end=' ')
#     fatorial *= i
#     i += 1
# print('O fatorial de {} é {}'.format(num, fatorial))
    
