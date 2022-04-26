'''Refaça o desafio 009 mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for'''

numero = int(input('Digite um número: '))
for i in range(1, 11):
    resultado = numero * i
    print('{} x {} = {}' .format(numero, i, resultado))
