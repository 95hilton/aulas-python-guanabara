"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar;
- Se é a hora de se alistar
- Se já passou do tempo do alistamento

Seu programa também deveria mostrar o tempo que falta ou que passou do prazo"""

from datetime import date

sexo = str(input('Digite seu sexo: [M] para Masculino [F] para Feminino: ')).upper()

if sexo == 'F':
    print('Você não precisará se alistar!')
elif sexo == 'M':
    ano = int(input('Digite o seu ANO de NASCIMENTO: '))
    idade = date.today().year - ano
    tempo_alistamento = 18 - idade

    if idade < 18:
        print('Você ainda deverá se alistar, quando completar 18 ANOS!\nIdade atual: {} anos\nTempo que ainda falta para alistar: {} anos' .format(idade, tempo_alistamento))
    elif idade > 18:
        print('Já passou {} anos do tempo do alistamento!\nIdade atual: {} anos'.format(tempo_alistamento*-1, idade))
    else:
        print('É hora de se alistar!\nIdade atual: {} anos'.format(idade))

else:
    print('Não compreendi sua resposta. Tente novamente mais tarde!')