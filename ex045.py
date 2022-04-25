"""Crie um programa que faça o computador jogar JOKENPÔ com você"""

import emoji
from random import randrange
print('Vamos jogar!!!')
usuario = int(input('Escolha sua opção (de 1 a 3):'
                    '\n1 - Pedra'
                    '\n2 - Papel'
                    '\n3 - Tesoura'))
computador = randrange(1, 3, 1)

if usuario == 1 and computador == 3 or usuario == 2 and computador == 1:
    print('Você escolheu PEDRA')
elif usuario == 1 and computador == 3 or usuario == 2 and computador == 1:
    print('Você escolheu PAPEL')
elif usuario == 3:
   print('Você escolheu TESOURA')
else:
    print('Opção inexistente. Volte mais tarde!')



