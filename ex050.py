'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o'''
numeros = []
soma = 0

for i in range(0, 6):
    numeros.append(int(input('Digite um número inteiro: ')))
    if numeros[i] % 2 == 0:
        soma += numeros[i]

print('A soma entre os números PARES é: {}' .format(soma))
