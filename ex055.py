'''Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''
import numpy
peso = []

for i in range(0, 5):
    peso.append(float(input('Digite o peso da {}ª pessoa: ' .format(i+1))))

ordenado = numpy.sort(peso)

print('Maior peso: {} Kg\nMenor peso: {} Kg' .format(ordenado[4], ordenado[0]))
