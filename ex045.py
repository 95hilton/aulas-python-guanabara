"""Crie um programa que faça o computador jogar JOKENPÔ com você"""

import emoji
from random import randrange
from time import sleep
print('Vamos jogar!!!')
usuario = int(input('Escolha sua opção (de 1 a 3):'
                    '\n1 - Pedra'
                    '\n2 - Papel'
                    '\n3 - Tesoura'
                    '\nEscolha: '))
computador = randrange(1, 3)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
if usuario == 1 and computador == 3:
    print(emoji.emojize('Você escolheu PEDRA \u270A e eu escolhi TESOURA \u270C\uFE0F.\nParabéns! Você GANHOU!'))
elif usuario == 2 and computador == 1:
    print(emoji.emojize('Você escolheu PAPEL \u270B e eu escolhi PEDRA \u270A.\nParabéns! Você GANHOU!'))
elif usuario == 3 and computador == 2:
    print(emoji.emojize('Você escolheu TESOURA \u270C\uFE0F e eu escolhi PAPEL \u270B.\nParabéns! Você GANHOU!'))
elif usuario == 3 and computador == 1:
    print(emoji.emojize('Você escolheu TESOURA \u270C\uFE0F e eu escolhi PEDRA \u270A.\nEU GANHEI!'))
elif usuario == 1 and computador == 2:
    print(emoji.emojize('Você escolheu PEDRA \u270A e eu escolhi PAPEL \u270B.\nEU GANHEI!'))
elif usuario == 2 and computador == 3:
    print(emoji.emojize('Você escolheu PAPEL \u270B e eu escolhi TESOURA \u270C\uFE0F.\nEU GANHEI!'))
else:
    print(emoji.emojize('Deu empate!!!\U0001f615'))



