'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai lera a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

jogador = {}
gols = []
total = 0
jogador['nome'] = str(input('Digite o nome do jogador: '))
jogador['partidas'] = int(input(f'Digite quantas partidas o jogador {jogador["nome"]} jogou: '))

for i in range(0, jogador['partidas']):
    gol = int(input(f'Quantos gols na partida {i+1}? '))
    gols.append(gol)
    total += gol

jogador['gols'] = gols
jogador['total'] = total

print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for g, v in enumerate(gols):
    print(f'Na partida {g+1}, o jogador fez {v} gols.')

print(f'Total de gols: {jogador["total"]}')
