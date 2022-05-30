'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex:
n = leiaInt('Digite um n')'''


def leiaInt(n):
    while True:
        num = input(n)
        if num.isnumeric():
            return num
        else:
            print('\033[0;31mERRO, digite um número inteiro!\033[m')


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}!')
