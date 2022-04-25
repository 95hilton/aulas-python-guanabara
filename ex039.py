"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar;
- Se é a hora de se alistar
- Se já passou do tempo do alistamento

Seu programa também deveria mostrar o tempo que falta ou que passou do prazo"""

from datetime import date

ano = int(input('Digite o seu ANO de NASCIMENTO: '))
idade = date.today().year - ano

if idade < 18:
    print('Você ainda deverá se alistar, quando completar 18 ANOS!\nIdade atual: {} anos' .format(idade))
elif idade > 18:
    print('Já passou do tempo do alistamento!\nIdade atual: {} anos'.format(idade))
else:
    print('É hora de se alistar!\nIdade atual: {} anos'.format(idade))
