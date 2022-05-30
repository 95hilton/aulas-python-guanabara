'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.'''


def voto(nascimento):
    from datetime import datetime
    anoatual = datetime.now().year
    idade = anoatual - nascimento
    if idade < 16:
        return f'Com {idade} anos, você não pode votar!'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos, o seu voto é OPCIONAL.'
    else:
        return f'Com {idade} anos, o seu voto é OBRIGATÓRIO.'


ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
