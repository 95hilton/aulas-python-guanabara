#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
valor = float(input('Insira quanto dinheiro você tem em Reais: '))
cotacao_dolar = float(4.70)
poder_de_compra = valor / cotacao_dolar

#formata o "poder_de_compra" para utilizar duas casas decimais antes de imprimir
fpcompra = "{:.2f}".format(poder_de_compra)

#formata a "cotacao_dolar" para utilizar duas casas decimais antes de imprimir
fcotacao = "{:.2f}".format(cotacao_dolar)

print('Você pode comprar US${}. \nA cotação do Dolar é: US$1.00 = R${}' .format(fpcompra, fcotacao))