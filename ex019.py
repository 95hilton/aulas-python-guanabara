# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
alunos = []

for i in range(1, 5):
    alunos.append(input('Digite o nome do aluno {}: ' .format(i)))

escolhido = choice(alunos)

print('O aluno escolhido foi: {}' .format(escolhido))
