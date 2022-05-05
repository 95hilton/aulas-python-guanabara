'''Faça um programa que leia nome c peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
- Quantas pessoas foram cadastradas
- Uma listagem com as pessoas mais pesadas
- Uma listagem com as pessoas mais leves'''
pessoas = []
info = []
maior = 0
menor = 0

while True:
    info.append(str(input('Digite o nome da pessoa: ')))
    info.append(float(input('Digite o peso: ')))

    if len(pessoas) == 0:
        maior = menor = info[1]
    else:
        if info[1] > maior:
            maior = info[1]
        if info[1] < menor:
            menor = info[1]

    pessoas.append(info[:])
    info.clear()

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continua == 'N':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'Menor peso: {menor} kg', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'|{p[0]}|', end=' ')
print()
print(f'Maior peso: {maior} kg', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'|{p[0]}|', end=' ')


