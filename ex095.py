'''Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador'''

estatisticas = []
jogador = {}
gols = []
total = 0

continua = ' '
while True:
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    jogador['partidas'] = int(input(f'Digite quantas partidas o jogador {jogador["nome"]} jogou: '))

    for i in range(0, jogador['partidas']):
        gol = int(input(f'Quantos gols na partida {i+1}? '))
        gols.append(gol)
        total += gol

    jogador['gols'] = gols.copy()
    gols.clear()
    jogador['total'] = total
    estatisticas.append(jogador.copy())
    jogador.clear()
    total = 0
    while True:
        continua = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if continua in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if continua == 'N':
        for i in estatisticas[0].keys():
            print(f'{i:<15}', end='')
        print()
        print('=' * 50)
        for k, v in enumerate(estatisticas):
            print(f'{k:>4}', end=' ')
            for i in v:
                print(f'{str(v[i]):<15}', end=' ')
            print()

        exibir = int(input('Mostrar dados de qual jogador? (Selecione pelo índice ou 999 para sair) '))
        while True:
           if exibir == 999:
                break
           elif exibir >= len(estatisticas):
               print(f'ERRO! Não existe jogador com código {exibir}. Tente novamente.')
               exibir = int(input('Mostrar dados de qual jogador? (Selecione pelo índice ou 999 para sair) '))
           else:
               print(f'---Levantamento do jogador {estatisticas[exibir]["nome"]}')
               for k, v in enumerate(estatisticas[exibir]["gols"]):
                    print(f'No jogo {k+1} fez {v} gols')

               exibir = int(input('Mostrar dados de qual jogador? (Selecione pelo índice ou 999 para sair) '))

        break
