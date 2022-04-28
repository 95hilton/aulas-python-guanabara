'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso'''

valorA = int(input('Digite o primeiro valor: '))
valorB = int(input('Digite o segundo valor: '))
opcao = 0

while opcao != 5 or opcao == 4:

    opcao = int(input('''\n[1] somar
                        \n[2] multiplicar
                        \n[3] maior
                        \n[4] novos números
                        \n[5] sair do programa
                        \nDigite a opção desejada: '''))

    if opcao == 1:
        soma = valorA + valorB
        print('A soma entre {} e {} é: {}'.format(valorA, valorB, soma))

    elif opcao == 2:
        mult = valorA * valorB
        print('A multiplicação entre {} e {} é: {}'.format(valorA, valorB, mult))

    elif opcao == 3:
        if valorA > valorB:
            print('O número {} é maior do que {}.'.format(valorA, valorB))
        elif valorA < valorB:
            print('O número {} é maior do que {}.'.format(valorB, valorA))
        else:
            print('Os números são iguais.')

    elif opcao == 4:
        print('\nIniciando novamente....\n')
        valorA = int(input('Digite o primeiro valor: '))
        valorB = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Encerrando programa.')
