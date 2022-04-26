'''Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores'''
from datetime import date
ano = date.today().year
nascimento = []
maiores = 0
menores = 0

for i in range(0, 7):
    nascimento.append(int(input('Digite o ano de nascimento da {}ª pessoa: ' .format(i+1))))
    idade = ano - nascimento[i]
    if idade >= 21:
        maiores = maiores + 1
    else:
        menores = menores + 1
print('{} pessoas já atingiram a maioridade e {} pessoas ainda não atingiram a maioridade.' .format(maiores, menores))
