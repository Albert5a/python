num = [2, 5, 9, 1]
num[2] = 3 # add número 3 no lugar do índice 2
num.append(7) # add número 7 no final, criando mais um ídice
print(num)
num.sort() # coloca os números em ordem crescente
print(num)
num.sort(reverse=True) # coloca os números em ordem decrescente
print(num)
num.insert(2, 0) # isere o número 0 na posição 2
print(num)
print(len(num))
num.pop() # elimina o último índice
print(num)
num.pop(2) # elimina o índice 2
num.remove(7) # removerá o primeiro elemento 7 da lista
print(num)