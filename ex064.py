'''Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condiçao de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag)'''

num = 0
cont = 0
soma = 0

while num != 999:

    soma += num
    num = int(input('Digite um número qualquer, ou 999 para parar: '))
    cont += 1

print('Foram digitados {} números e a soma foi {}' .format(cont-1, soma))
