'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A - Quantos números foram digitados,
B - A lista de valores ordenada de forma decrescente:
C- Se o valor 5 foi digitado e está ou não na lista'''
valores = []

while True:
    valores.append(int(input('Digite um valor: ')))

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Você deseja continuar? [S/N] ')).strip().upper()

    if continua == 'N':
        print(f'Foram digitados {len(valores)} números.\n')
        valores.sort(reverse=True)
        print(f'Lista de valores {valores}\n')
        if 5 in valores:
            print('O número 5 foi digitado!\n')
        else:
            print('O número 5 NÃO foi digitado!\n')
        break
