'''Crie uma tupla preenchida com os 20 preimeiros colocados da Tabela do Campeonato Brasieliro de Futebol, na ordem de colocação.
Depois mostre:
A- Apenas os 5 primeiros colocados;
B- Os últimos 4 colocados da tabela
C- Uma lista com os times em ordem alfabética.
D- Em que posição na tabela está o time da Chapecoense.
'''
tabela = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Athlético-PR', 'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corínthians', 'Chapecoense', 'Ceará', 'Vasco', 'Sport', 'América-MG', 'Vitória', 'Paraná')

libertadores = tabela[:5]

rebaixados = tabela[-4:]

ordenados = sorted(tabela)

chapecoense = tabela.index('Chapecoense')+1

print(f'\nOs 5 primeiros colocados no campeonato foram:')
for pos, time in enumerate(libertadores):
    print(f'{pos+1}º: {time}')

print(f'\nOs quatro últimos colocados foram:')
for pos, time in enumerate(rebaixados):
    print(f'{pos+17}º: {time}')

print(f'\nA classificação em ordem alfabética foi:')
for pos, time in enumerate(ordenados):
    print(f'{pos+1}º: {time}')

print(f'A Chapecoense terminou na {chapecoense}ª posição. ')
