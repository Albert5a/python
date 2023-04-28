from random import randint
while True:
    print('-='*15)
    escolhaJogador = str(input('Par ou ímpar [P/I]: ').upper())
    print('-='*15)
    ncomputador = randint(0, 5)
    njogador = int(input('Jogue o seu número: '))
    print('-='*15)
    resultado = ncomputador + njogador
    if escolhaJogador == 'P' and resultado % 2 == 0:
        print(f'Deu {resultado}. Parabéns, você venceu. Jogue mais uma vez!')
    elif escolhaJogador == 'I' and resultado % 2 == 1:
        print(f'Deu {resultado}. Parabéns, você venceu. Jogue mais uma vez!')
    else:
        break
print(f'Deu {resultado}. Você perdeu. FIM!')