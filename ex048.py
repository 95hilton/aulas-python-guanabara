'''Faça um programa que calcule a soma entre todos os números impares que são multiplos de tres e se encontrem no intervalo entre 1 e 500'''

soma = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i

print('O resultado da soma é: {}' .format(soma))
