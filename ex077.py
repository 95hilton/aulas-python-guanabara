'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar para cada palavra, quais são as suas vogais'''

palavras = ('macarrao', 'sabonete', 'arroz', 'berinjela', 'cafe')

for i in palavras:
    print(f'\nNa palavara {i.upper()} temos: ', end='')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
