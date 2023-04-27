print('-='*10)
print('GERANDO FIBONACCI')
print('-='*10)
fiboPast = 0
fibo = 1
fiboFuture = 1
c = 2
terms = int(input('Quantos termos você quer ver? '))
print(fiboPast, fibo, end=' ')
while c < terms:
    print(fiboFuture, end=' ')
    fiboPast = fibo
    fibo = fiboFuture
    fiboFuture = fiboPast + fibo
    c += 1
print('FIM')
