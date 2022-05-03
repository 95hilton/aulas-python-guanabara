'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados respectivamente.
Ao final mostre o conteúdo das três listas geradas.'''
'''ler apenas os valores no primeiro loop'''
lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Digite um número: ')))

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N]: ')).strip().upper()

    if continua == 'N':
        for l in lista:
            if l % 2 == 0:
                pares.append(l)
            else:
                impares.append(l)

        print(f'A lista completa é: {lista}')
        print(f'A lista de pares é: {pares}')
        print(f'A lista de ímpares é: {impares}')
        break
