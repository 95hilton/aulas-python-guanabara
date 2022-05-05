'''Aprimore o desafio anterior, mostrando no final:
- A soma de todos os valores pares digitados
- A soma dos valores da terceira coluna
- O maior valor da segunda linha'''
valores = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
terceira = 0
maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        valores[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if valores[l][c] % 2 == 0:
            pares += valores[l][c]
        if c == 2:
            terceira += valores[l][c]
        if l == 1 and maior < valores[l][c]:
            maior = valores[l][c]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{valores[l][c]:^5}]', end='')
    print()

print(f'A soma dos números pares é: {pares}')
print(f'A soma dos valores da terceira coluna é {terceira}')
print(f'O maior valor da segunda linha é: {maior}')
