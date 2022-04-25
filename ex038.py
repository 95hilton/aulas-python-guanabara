"""Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O priemiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais"""

numeros = []

for i in range(1, 3):
    numeros.append(int(input('Digite um o {}º número: ' .format(i))))

if numeros[0] > numeros[1]:
    print('O PRIMEIRO número é maior!!\nNúmeros digitados: {} e {}.' .format(numeros[0], numeros[1]))
elif numeros[0] < numeros[1]:
    print('O SEGUNDO número é maior!!\nNúmeros digitados: {} e {}.' .format(numeros[0], numeros[1]))
else:
    print('AMBOS OS NÚMEROS SÃO IGUAIS!\nNúmeros digitados: {} e {}.' .format(numeros[0], numeros[1]))

