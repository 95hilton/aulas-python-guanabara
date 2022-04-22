"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
primeiro = Ana
último = Souza"""

nome = str(input('Digite seu nome completo: ')).strip()
spl = nome.split()

print('Primeiro nome: {}\nÚltimo nome: {}' .format(spl[0], spl[len(spl)-1]))
