"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- À vista dinheiro/ cheque: 10% de desconto;
- À vista no cartão: 5% de desconto;
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão 20% de juros"""

preco = float(input('Digite o preço normal do produto: R$ '))
pagamento = int(input('''Selecione a forma de pagamento:
                        \n1 - À vista dinheiro/ cheque
                        \n2 - À vista no cartão
                         \n3 - Em até 2x no cartão
                         \n4 - 3x ou mais no cartão
                         \n'''))
total = 0
if pagamento == 1:
    total = preco - (preco*0.1)
    print('Você irá pagar À VISTA NO DINHEIRO/ CHEQUE, e terá que pagar o valor de R$ {:.2f}' .format(total))
elif pagamento == 2:
    total = preco - (preco*0.05)
    print('Você irá pagar À VISTA NO CARTÃO, e terá que pagar o valor de R$ {:.2f}' .format(total))
elif pagamento == 3:
    total = preco
    print('Você irá pagar EM até 2X NO CARTÃO, e terá que pagar o valor de R$ {:.2f}' .format(total))
elif pagamento == 4:
    total = preco + (preco*0.2)
    print('Você irá pagar EM até 3X OU MAIS NO CARTÃO, e terá que pagar o valor de R$ {:.2f}' .format(total))
else:
    print('Formato de pagamento inválido. Tente novamente mais tarde!')