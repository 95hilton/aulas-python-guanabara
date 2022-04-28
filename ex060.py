'''Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5!=5x4x3x2x1 = 120'''

numero = int(input('Digite um número para calcular seu fatorial: '))
fatorial = 1

print('Resultado de {}! = ' .format(numero), end=' ')
while numero > 0:
    print('{}'.format(numero), end='')
    if numero > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    fatorial *= numero
    numero -= 1

print(' {}' .format(fatorial))
