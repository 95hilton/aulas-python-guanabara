'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de nascimento do grupo
C) Uma lista com todas as mulheres
D) Uma lista com todas as pessoas com idade acima da média'''
contador = 0
media = 0
idades = 0
pessoa = dict()
lista = list()
mulheres = list()
acima = list()

while True:
    pessoa['nome'] = str(input('Digite o nome: '))

    while True:
        pessoa['sexo'] = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Digite apenas M ou F')

    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])

    pessoa['idade'] = int(input('Digite a idade: '))
    idades += pessoa['idade']

    contador += 1
    media = idades / contador

    lista.append(pessoa.copy())
    pessoa.clear()

    while True:
        continua = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if continua in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if continua == 'N':
        print(lista)
        print(f'O grupo tem {len(lista)} pessoas.')
        print(f'A média de idade é de {media :.1f} anos')
        print(f'As mulheres cadastradas foram:', end=' ')
        for m in mulheres:
            print(m, end=' ')
        print()
        print(f'Lista de pessoas com idade acima da média: ')
        for p in lista:
            if p['idade'] > media:
                print(f'Nome: {p["nome"]}'
                      f'\nSexo:{p["sexo"]}'
                      f'\nIdade:{p["idade"]}')
                print('==============')
        break
