# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math

oposto = float(input('Digite o comprimento do cateto oposto: '))
adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(oposto, adjacente)

print('O comprimento da hipotenusa é: {}' .format(hipotenusa))