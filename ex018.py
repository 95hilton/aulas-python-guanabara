# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import radians, sin, cos, tan

angulo = int(input('Digite o ângulo desejado: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O seno corresponde a: {:.2f}\nO cosseno corresponde a: {:.2f}\nA tangente corresponde a: {:.2f}\n' .format(seno, cosseno, tangente))
