'''Faça um programa que jogue par ou impar com o computador.
O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
vitoriasH = 0

while True:
    opcao = str(input('Você quer Par ou Ímpar?\nDigite P ou I: ')).strip().upper()[0]
    humano = int(input('Digite quanto vai jogar: '))
    computador = randint(1, 2)
    resultado = humano + computador

    if opcao == 'P':
        if resultado % 2 != 0:
            print(f'ERROOOOUU! {humano} + {computador} = {resultado} - DEU ÍMPAR')
            print(f'Você perdeu, e teve {vitoriasH} vitórias consecutivas!')
            break
        else:
            print(f'Você ganhou essa! {humano} + {computador} = {resultado} - DEU PAR')
            vitoriasH += 1
    elif opcao == 'I':
        if resultado % 2 == 0:
            print(f'ERROOOOUU! {humano} + {computador} = {resultado} - DEU PAR')
            print(f'Você perdeu, e teve {vitoriasH} vitórias consecutivas!')
            break
        else:
            print(f'Você ganhou essa! {humano} + {computador} = {resultado} - DEU ÍMPAR')
            vitoriasH += 1
