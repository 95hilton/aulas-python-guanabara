'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos total serão gerados e vai sortear 6 números entre 1 c 60 para cada jogo, cadastrando tudo em uma lista composta.'''
from asyncio import sleep
from random import randint
lista = []
jogos = []
qtd = int(input('Quantos total você deseja gerar? '))
total = 1
while total <= qtd:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

for i, l in enumerate(jogos):
    print(f'Aposta {i+1} criada: {l}')

