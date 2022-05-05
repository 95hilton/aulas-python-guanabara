'''Crie um programa onde o usuário possa digitar sete valores numéricos c cadastre-os em uma lista única que mantenha separados os valores pares c ímpares.
No final, mostre os valores pares c ímpares em ordem crescente.
trabalhe com apenas uma lista com listas internas'''
valores = [[], []]
valor = 0
for i in range(0, 7):
    valor = int(input(f'Ditie o {i+1}º valor: '))

    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
valores[0].sort()
print(f'Valores pares: {valores[0]}')
valores[1].sort()
print(f'Valores ímpares: {valores[1]}')
