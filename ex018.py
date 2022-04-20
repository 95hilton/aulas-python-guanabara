# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math

angulo = int(input('Digite o ângulo desejado: '))
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print('O seno corresponde a: {:.2f}\nO cosseno corresponde a: {:.2f}\nA tangente corresponde a: {:.2f}\n' .format(seno, cosseno, tangente))
