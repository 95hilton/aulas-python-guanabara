'''Crie um módulo chamado modeda.py que tenha as funções incorporadas aumentar(), diminuir, dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções'''

import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {p} é {moeda.metade(p)}')
print(f'O dobro de R$ {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')


