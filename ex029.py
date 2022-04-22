"""Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite"""

velocidade = float(input('Digite a velocidade do carro em Km/H: '))
multa = 0
cores = {'limpa': '\033[m',
         'verdebold': '\033[1;32m',
         'vermelhobold': '\033[1;31m'}
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você foi multado em {}R$ {:.2f}{}' .format(cores['vermelhobold'], multa, cores['limpa']))
else:
    print('{}Você não foi multado!{}' .format(cores['verdebold'], cores['limpa']))
