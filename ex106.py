'''Faça um mini-sistema que utilize o interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra "FIM", o programa se encerrará
OBS: Use cores'''


def banner(cor, texto=' '):
    if cor == 'verde':
        print(f'\033[1;42m{texto}\033[m')
    elif cor == 'azul':
        print(f'\033[1;44m{texto}\033[m')
    elif cor == 'branco':
        print(f'\033[1;107m	\033[1;30m{texto}')
    elif cor == 'vermelho':
        print(f'\033[1;41m{texto}\033[m')
    elif cor == 'nulo':
        print('\033[m')


def pyHelp():
    banner('verde', 'SISTEMA DE AJUDA PYHELP')
    while True:
        entrada = input('Digite a função ou biblioteca: ').upper().strip()
        if entrada == 'FIM':
            banner('vermelho', 'ATÉ LOGO!')
            break
        else:
            banner('azul', f'Acessando o manual do comando \'{entrada}\'...')
            banner('branco')
            help(entrada)
            banner('nulo')


pyHelp()
