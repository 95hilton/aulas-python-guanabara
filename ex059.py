'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso'''

opcao = 0

while opcao != 5 or opcao == 4:
    valorA = int(input('Digite o primeiro valor: '))
    valorB = int(input('Digite o segundo valor: '))
    opcao = int(input('''Digite a opção desejada:\n 
                        \n[1] somar
                        \n[2] multiplicar
                        \n[3] maior
                        \n[4] novos números
                        \n[5] sair do programa
                        \n'''))

    if opcao == 1:
        soma = valorA + valorB
        print('A soma entre {} e {} é: {}'.format(valorA, valorB, soma))
        opcao = 5
    elif opcao == 2:
        mult = valorA * valorB
        print('A multiplicação entre {} e {} é: {}'.format(valorA, valorB, mult))
        opcao = 5
    elif opcao == 3:
        if valorA > valorB:
            print('O número {} é maior do que {}.'.format(valorA, valorB))
        elif valorA < valorB:
            print('O número {} é maior do que {}.'.format(valorB, valorA))
        else:
            print('Os números são iguais.')
            opcao = 5
    elif opcao == 4:
        print('\nIniciando novamente....\n')

print('Encerrando programa.')
