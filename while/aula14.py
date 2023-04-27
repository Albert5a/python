# for c in range (1, 10):
#     print(c)
# print('Fim')

# c = 1
# while c < 10:
#     print(c)
#     c = c + 1
# print ('Fim')

n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('FIM')
print('Par: {}'.format(par))
print('Impar: {}'.format(impar))