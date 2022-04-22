"""Escreva um programa que faça o computador pensar um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
Este programa deverá escrever na tela se o usuário venceu ou perdeu."""
from random import randrange
from time import sleep
numero = int(input('Digite o número inteiro entre 0 e 5, que você acha que eu escolhi: '))

sorteado = int(randrange(0, 5))
print('AGUARDE...')
sleep(3)
if numero == sorteado:
    print('Você venceu! Eu realmente escolhi o número {}!' .format(sorteado))
if numero > 5:
    print('Não vale roubar! É só de 0 a 5. Tente de novo mais tarde!')
else:
    print('Você perdeu! Eu escolhi o número {}!' .format(sorteado))