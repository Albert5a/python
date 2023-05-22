a = [1, 3, 5, 7]
b = a[:] # b recebe cópia da lista a
b[1] = 2
print(f'Lista A: {a}')
print(f'Lista B: {b}')