'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''
soma = 0
cont = 0
while True:
    numero = int(input('Digite um número, ou 999 para parar: '))
    cont += 1
    if numero == 999:
        break
    soma += numero
print(f'Foram digitados {cont-1} números, e a soma deles foi: {soma}')
