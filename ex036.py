"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado."""
cores = {'limpa': '\033[m',
         'verdebold': '\033[1;32m',
         'vermelhobold': '\033[1;31m'}

casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o seu salário: R$ '))
anos = int(input('Digite em quantos anos você vai pagar: '))
prestacao = casa/(anos*12)
percent_salario = prestacao/casa

if prestacao > salario * 0.30:
    print('Não será possível realizar o empréstimo, pois a parcela é {} MAIOR {} do que 30% do seu salário!\nSalário: {:.2f}\nValor das parcelas: {:.2f}\nValor do Imóvel: {:.2f}'.format(cores['vermelhobold'], cores['limpa'], salario, prestacao, casa))
else:
    print('{}Parabéns!! Sua casa própria está à caminho! Vamos realizar o empréstimo!\nSalário: {:.2f}\nValor das parcelas: {:.2f}\nValor do Imóvel: {:.2f}{}' .format(cores['verdebold'], salario, prestacao, casa, cores['limpa']))
