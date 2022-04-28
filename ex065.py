'''Crie um programa que leia varios numeros inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
from numpy import sort
from numpy import mean
numeros = []
continua = 'S'

while continua == 'S':
    numeros.append(int(input('Digite um número: ')))
    continua = str(input('Você deseja continuar? [S]im ou [N]ão: ')).upper().strip()

ordenados = sort(numeros)

media = mean(numeros)

print('O maior valor digitado: {}' .format(ordenados[len(ordenados)-1]))
print('O menor valor digitado: {}'.format(ordenados[0]))
print('A média dos números digitados é: {:.2f}' .format(media))
