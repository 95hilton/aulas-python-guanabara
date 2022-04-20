# Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6

import math

num = float(input('Digite um número: '))

print('A porção inteira de {} é: {}'.format(num, math.floor(num)))
