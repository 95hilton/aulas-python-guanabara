'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
numero = ''
valores = []

while True:
    numero = int(input('Digite um valor numérico: '))

    if valores.__contains__(numero):
        print(f'O número {numero} já existe na lista. Não será adicionado novamente.')
    else:
        valores.append(numero)
        print('Valor adicionado com sucesso!')

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S] ou [N]: ')).upper().strip()

    if continua == 'N':
        valores.sort()
        print(f'Os valores digitados foram: {valores}')
        break
