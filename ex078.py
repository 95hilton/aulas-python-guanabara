'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''
'''considere repetição de numeros'''
valores = []
maior = 0
menor = 0

for i in range(0, 5):
    valores.append(int(input(f'Digite o {i+1}º valor: ')))
    if i == 0:
        maior = menor = valores[i]

    for v in valores:
        if v > maior:
            maior = v
        if v < menor:
            menor = v

print(f'O maior valor digitado foi: {maior} nas posições', end=' ')
for n, l in enumerate(valores):
    if l == maior:
        print(f'{n}...', end='')
print()
print(f'O menor valor digitado foi: {menor} nas posições', end=' ')
for n, l in enumerate(valores):
    if l == menor:
        print(f'{n}...', end='')
print()


