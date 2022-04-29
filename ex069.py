'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
 A - quantas pessoas tem mais de 18 anos.
 B - quantos homens foram cadastrados.
 C - Quantas mulheres tem menos de 20 anos'''

maior18 = 0
homens = 0
menor20 = 0

while True:
    idade = int(input('Digite a idade: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo M ou F: ')).strip().upper()[0]

    continua = ' '
    while continua not in'SN':
        continua = str(input('Você deseja continuar? [S]im ou [N]ão? ')).strip().upper()[0]

    if idade > 18:
        maior18 += 1

    if idade < 20 and sexo == 'F':
        menor20 += 1

    if sexo == 'M':
        homens += 1

    if continua != 'S':
        print(f'''Há {maior18} pessoas com mais de 18 anos.\nHá {homens} homens cadastrados.\nHá {menor20} mulheres com menos de 20 anos cadastradas.''')
        break
