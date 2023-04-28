n = s = c = 0
while True:
    n = float(input('Digite um numero: (999 para parar) '))
    if n == 999:
        break
    s += n
    c += 1
print(f'{c} números digitados. A soma vale {s:.2f}')