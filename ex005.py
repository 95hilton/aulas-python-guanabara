#Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e o seu antecessor:

numero = int(input('Digite um número: '))
print('O antecessor de {} é: {}. \nO seu sucessor é: {}'.format(numero, numero-1, numero+1))
