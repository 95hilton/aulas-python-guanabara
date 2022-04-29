'''Crie um programa que leia o nome e preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:

A - Qual é o total gasto na compra.
B - Quantos produtos custam mais de R$ 1000.
C - Qual é o nome do produto mais barato'''
total = 0
acima_mil = 0
preco_barato = 0
nome_barato = ''

while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: R$ '))

    total += preco
    if preco > 1000:
        acima_mil += 1

    if preco_barato == 0 or preco < preco_barato:
        preco_barato = preco
        nome_barato = nome

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar inserindo preços? [S] ou [N]: ')).strip().upper()
    if continua == 'N':
        print(f'''Finalizando programa...
                \nTotal Gasto: R$ {total:.2f}\nQtd. de produtos acima de R$ 1000: {acima_mil}\nNome do produto mais barato: {nome_barato}''')
        break
