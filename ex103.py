'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.'''


def ficha(nome='', gols=''):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '' or gols.isnumeric() is False:
        gols = 0
    return nome, gols


n = str(input('Digite o nome do jogador: '))
g = str(input('Digite o número de gols feitos: '))

result = ficha(n, g)

print(f'O jogador {result[0]} fez {result[1]} gols')
