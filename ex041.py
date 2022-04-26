"""A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com sua idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SENIOR
- Acima: MASTER"""
from datetime import date

nascimento = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - nascimento

if idade <= 9:
    print('Sua idade é {} anos e sua categoria é MIRIM!' .format(idade))
elif idade <= 14:
    print('Sua idade é {} anos e sua categoria é INFANTIL!' .format(idade))
elif idade <= 19:
    print('Sua idade é {} anos e sua categoria é JUNIOR!' .format(idade))
elif idade <= 25:
    print('Sua idade é {} anos e sua categoria é SENIOR!'.format(idade))
else:
    print('Sua idade é {} anos e sua categoria é MASTER!' .format(idade))
