'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar(). A priemira função vai sortear 5 números e vai coloca-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.'''
from random import randrange
from time import sleep
numeros = list()


def sorteio():
    print('Sorteando 5 valores da lista: ', end=' ')
    for i in range(0, 5):
        sleep(0.5)
        n = randrange(0, 11)
        numeros.append(n)
        print(n, end=' ')
    print()
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for l in lista:
        if l % 2 == 0:
            soma += l
    print(f'Somando os valores pares de {lista}, temos o total {soma}')


sorteio()
somaPar(numeros)
