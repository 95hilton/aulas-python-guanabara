'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$ 1'''

valor = int(input('Digite o valor que deseja sacar: R$ '))

print(f'Você receberá: ')

while True:
    notas50 = valor//50
    resto = valor % 50

    notas20 = resto // 20
    resto = resto % 20

    notas10 = resto // 10
    resto = resto % 10

    notas1 = resto // 1

    if notas50 > 0:
        print(f'{notas50} notas de R$ 50')

    if notas20 > 0:
        print(f'{notas20} notas de R$ 20')

    if notas10 > 0:
        print(f'{notas10} notas de R$ 10')

    if notas1 > 0:
        print(f'{notas1} notas de R$ 1')

    break
