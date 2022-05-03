'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre os em uma lista, ja na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.'''
atual = ' '
valores = []

for i in range(0, 5):
    atual = int(input(f'Digite o {i + 1}º valor: '))

    if i == 0:
        valores.append(atual)
        print('Acicionado ao final da lista')
    elif atual > valores[len(valores)-1]:
        valores.append(atual)
        print('Acicionado ao final da lista')
    else:
        posicao = 0
        while posicao < len(valores):
            if atual <= valores[posicao]:
                valores.insert(posicao, atual)
                print(f'Acicionado à posição {posicao+1} da lista')
                break
            posicao += 1

print(f'Os valores digitados em ordem foram: {valores}')
