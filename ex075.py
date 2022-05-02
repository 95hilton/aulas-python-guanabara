'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A- Quantas vezes apareceu o valor 9
B- Em que posição foi digitado o primeiro valor 3
C- Quais foram os números pares'''

numeros = (int(input('Digite o 1º número: ')),
           int(input('Digite o 2º número: ')),
           int(input('Digite o 3º número: ')),
           int(input('Digite o 4º número: ')))
pares = []

if numeros.count(9) > 0:
    print(f'\nO número 9 foi digitado {numeros.count(9)} vezes.')
else:
    print('\nO número 9 não foi digitado nenhuma vez.')

if 3 in numeros:
    print(f'\nO primeiro valor 3 foi digitado na posição {numeros.index(3)}')
else:
    print('\nO número 3 não foi digitado nenhuma vez.')

for i in numeros:
    if i % 2 == 0:
        pares.append(i)

if len(pares) > 0:
    print(f'\nNumeros pares: {pares}')
else:
    print('\nNão existem números pares na lista.')

