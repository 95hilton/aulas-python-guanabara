"""Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$ 0,50 por KM para viagens de até 200KM e R$0,45 para viagens mais longas."""

distancia = float(input('Digite a distância da viagem: '))
preco = 0
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print('O valor da sua passagem é: R${:.2f}' .format(preco))
