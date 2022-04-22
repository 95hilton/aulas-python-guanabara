"""Faça um programa que leia três números e mostre qual é o maior e qual é o menor"""
from numpy import sort

numeros =[]

for i in range(0, 3):
    numeros.append(int(input('Digite um número: ')))

ordenados = sort(numeros)

print('O maior número é: {}{}{}\nO menor número é: {}{}{}' .format('\033[1;32m', ordenados[2], '\033[m', '\033[1;31m', ordenados[0], '\033[m'))