n = s = 0
nome = 'José'
while True:
    n = float(input('Digite um numero: '))
    if n == 999:
        break
    s += n
print(f'{nome:^20}. A soma vale {s:.2f}')
print(f'{nome:20}. A soma vale {s:.2f}')
print(f'{nome:-^20}. A soma vale {s:.2f}')
print(f'{nome:->20}. A soma vale {s:.2f}')
print(f'{nome:-<20}. A soma vale {s:.2f}')