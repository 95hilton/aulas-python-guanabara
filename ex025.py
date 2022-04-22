# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

#Coleta o nome e remove espaços que usuário tenha colocado
nome = str(input('Digite o nome da pessoa: ')).strip()
#Tansforma todo o texto digitado em maiusculo para comparar com o texto do programa
print('Seu nome tem Silva? {}' .format('SILVA' in nome.upper()))
