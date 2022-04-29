'''Faça um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''

num = 0

while True:

    num = int(input('Digite um número para exibir a tabuada: '))
    if num < 0:
        print('FIM!')
        break

    for i in range(1, 11):
        result = num * i
        print(f'{num} x {i} = {result}')
