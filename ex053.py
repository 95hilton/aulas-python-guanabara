'''Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços'''

frase = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')
reversa = frase[::-1]

if frase == reversa:
    print('{} e {} são Palíndromos!' .format(frase, reversa))
else:
    print('{} e {} NÃO são Palíndromos!'.format(frase, reversa))

