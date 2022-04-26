'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''

primeiro = int(input('Digite o primeiro termo da Progressão Aritmética: '))
razao = int(input('Digite a razão da PA: '))
decimo = primeiro + 9 * razao
for i in range(primeiro, decimo+razao, razao):
    print('{}' .format(i), end=' -> ')
