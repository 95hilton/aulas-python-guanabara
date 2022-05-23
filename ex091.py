'''Crie um programa onde 4 jogadores joguem um dado e tenha resultados aleatórios. Guarde esses resultados em um dicionário.
No final, coloque essse dicionário em ordem sabendo que o vencedor tirou o maior número no dado.'''
from operator import itemgetter
from random import randint
from time import sleep

resultado = {}
ranking = []
print('Valores sorteados: ')
for c in range(0, 4):
    resultado[f'jogador{c+1}'] = randint(1, 6)
    print(f'O jogador{c+1} tirou {resultado[f"jogador{c+1}"]} no dado.')
    sleep(1)

print('Ranking dos jogadores: ')
ranking = sorted(resultado.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}ª lugar: {v[0]} com {v[1]}')
    sleep(1)
