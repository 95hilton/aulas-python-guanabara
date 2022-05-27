'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
a- De 1 até 10, de 1 em 1
b- de 10 até 0, de 2 em 2
c- Uma contagem personalizada'''
from time import sleep


def contador(inicio, fim, passo):
    if inicio < fim:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
        for c in range(inicio, fim+1, passo):
            sleep(0.5)
            print(c, end=' ')
        print('FIM!')
        print('=-' * 30)
    elif passo < 0:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
        for c in range(inicio, fim-1, passo):
            sleep(0.5)
            print(c, end=' ')
        print('FIM!')
        print('=-' * 30)
    elif passo == 0:
        print(f'Contagem de {inicio} até {fim} de 1 em 1:')
        for c in range(inicio, fim-1, -1):
            sleep(0.5)
            print(c, end=' ')
        print('FIM!')
        print('=-' * 30)
    elif inicio > fim:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
        for c in range(inicio, fim-1, -passo):
            sleep(0.5)
            print(c, end=' ')
        print('FIM!')
        print('=-' * 30)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
