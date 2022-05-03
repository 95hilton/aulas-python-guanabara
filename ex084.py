'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
- Quantas pessoas foram cadastradas
- Uma listagem com as pessoas mais pesadas
- Uma listagem com as pessoas mais leves'''
pessoas = []
info = []
while True:
    info.append(str(input('Digite o nome da pessoa: ')))
    info.append(float(input('Digite o peso: ')))
    pessoas.append(info)

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar? ')).strip().upper()
        if continua == 'N':
            print(f'Foram cadastradas {len(pessoas)} pessoas.')
            print('pessoas mais leves:')
    break
