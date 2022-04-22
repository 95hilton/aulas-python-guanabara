# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
alunos = []

for i in range(1, 5):
    alunos.append(input('Digite o nome do aluno {}: ' .format(i)))

print('A ordem de apresentação será: ')

shuffle(alunos)

print(alunos)
