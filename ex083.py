'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''
direita = 0
esquerda = 0

expressao = str(input('Digite a expressão: '))

for i in expressao:
    if '(' == i:
        esquerda += 1
    elif ')' == i:
        direita += 1

if direita == esquerda:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')
