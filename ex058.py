'''Melhore o jogo do DESAFIO 28 onde o computador vai pensar em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer'''

from random import randint
from time import sleep

numero = ''
contador = 0
sorteado = -1
while numero != sorteado:
    numero = int(input('Digite o número inteiro entre 0 e 10, que você acha que eu escolhi: '))
    contador += 1
    sorteado = int(randint(0, 11))
    print('AGUARDE...')
    sleep(3)
    if numero == sorteado:
        print('Você venceu! Eu realmente escolhi o número {}!' .format(sorteado))
        print('Você precisou de {} tentativas para me vencer.' .format(contador))
    elif numero > 10:
        print('Não vale roubar! É só de 0 a 10. Tente de novo!')
