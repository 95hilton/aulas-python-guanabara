"""A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com sua idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SENIOR
- Acima: MASTER"""

idade = int(input('Digite a sua idade: '))

if idade <= 9:
    print('Sua categoria é MIRIM!')
elif 9 < idade <= 14:
    print('Sua categoria é INFANTIL!')
elif 14 < idade <= 19:
    print('Sua categoria é JUNIOR!')
elif idade == 20:
    print('Sua categoria é SENIOR!')
else:
    print('Sua categoria é MASTER!')
