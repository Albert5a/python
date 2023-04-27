from time import sleep
x = int(input('Escolha um valor: '))
y = int(input('Escolha outro valor: '))
opcao = 0
resultado = 0
while opcao != 5:
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair')
    opcao = int(input('O que você deseja executar: '))
    if opcao == 1:
        resultado = x + y
        print('Soma de {} + {} = {}'.format(x, y, resultado))
    elif opcao == 2:
        resultado = x * y
        print('Multiplicação de {} * {} = {}'.format(x, y, resultado))
    elif opcao == 3:
        if x > y:
            print('O número {} é maior que o número {}'.format(x, y))
        else:
            print('O número {} é maior que o número {}'.format(y, x))
    elif opcao == 4:
        x = int(input('Escolha um valor: '))
        y = int(input('Escolha outro valor: '))
    else:
        print('Opção inválida, tente novamente uma opção válida')
    sleep(2)