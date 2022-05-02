'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular. '''

produtos = ('Arroz', 10.00, 'Feijão', 8.50, 'Picanha', 125.00)

for i in range(0, len(produtos), 2):
    print(f'{produtos[i]:.<30} R$ {produtos[i+1]:>7.2f}\n')
