'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estarão na tupla'''
from random import randint

tupla = (randint(0, 50), randint(0, 50), randint(0, 50), randint(0, 50), randint(0, 50))
maior = max(tupla)
menor = min(tupla)

print(f'\nOs números gerados foram: {tupla}')
print(f'\nMenor número: {menor}')
print(f'\nMaior número: {maior}')
