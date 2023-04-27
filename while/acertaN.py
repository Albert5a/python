from random import randint
# print('Eu sou um robô e escolhi um número, tente acertar!!!')
# numero = randint(0, 10)
# meuNumero = -1
# tentativas = 0
# while meuNumero != numero:
#     meuNumero = int(input('Tente escolher o mesmo número que eu. Qual é seu palpite: '))
#     tentativas += 1
# print('PARABÉNS. Eu também escolhi o número {}. Você acertou com {} tentativas!!!'.format(numero, tentativas))

# Professor
print('Bem vindo a versão do Gustavo Guanabar!')
computador = randint(0, 10)
print('Acabei de pensar em um número entre 0 e 10')
print('Tente acertar!!!')
acertou = False
tenta = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    tenta += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Meu número é maior!')
        elif jogador > computador:
            print('Meu número é menor!')
print('Acertou!!! Escolhi o numero {} e você acertou n {}ª tentativa!'.format(computador, tenta))

# Explicação do código do professor
# acertou = True
# O valor lógico boleano not investe os valores. 
# No código acima, acertou recebe False*, na estrutura de repetição, o not está invertendo o valor False para True, fazendo o loop continua (lembra do que o while só sai do loop se dá False)  depois ele coloca uma condição no loop para substituir *acertou para True e  consequentemente o not investe para False , saindo do loop.